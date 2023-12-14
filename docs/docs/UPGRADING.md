---
title: "Upgrading from MadelineProto v7 to v8"
description: "MadelineProto v8 is a major MadelineProto update, that removes a large number of long-deprecated APIs: I've created this upgrade checklist, to simplify the upgrade process.  "
nav_order: 29
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Upgrading from MadelineProto v7 to v8

MadelineProto v8 is a major MadelineProto update, that removes a large number of long-deprecated APIs: I've created this upgrade checklist, to simplify the upgrade process.  

A much simpler way to check for backwards incompatible changes is to scan your project using [Psalm](https://psalm.dev), it's truly a lifesaver!

Make sure to recreate the session too, as v7 sessions are not compatible with v8.

## Settings

The main breaking change is the removal of array settings, deprecated since v6.  
You can use object settings, instead, see [here &raquo;](https://docs.madelineproto.xyz/docs/SETTINGS.html) for the full documentation, here's a brief conversion example:

Before:

```php
$settings = ['app_info' => ['api_id' => 123456, 'api_hash' => 'xxx']];
```

After:

```php
$settings = (new \danog\MadelineProto\Settings\AppInfo)
    ->setApiId(123456)
    ->setApiHash('xxx');
```

See [here &raquo;](https://docs.madelineproto.xyz/docs/SETTINGS.html) for the full list of MadelineProto v8 settings.

Please note that since v8, usage of invalid setting setters and getters will throw an exception (in v7 those usages were simply ignored).  

## Amp v3

MadelineProto v8 switches to using fibers and Amp v3 libraries.  

Check out the changelogs of the [amphp](https://github.com/amphp/) libraries for a list of breaking changes introduced with the update of Amp v3.  

Regarding MadelineProto, `yield` support in the event handler was removed and the `async` and `loop` methods were removed, along with all the Generator combinator methods (`Tools::after`, `Tools::all`, `Tools::any`, `Tools::first`, et cetera).  

Instead, you can use the new async Amp v3 APIs, which do not require special keywords like `yield` anymore!

Before:

```php
class MyEventHandler {
    public function onUpdateNewMessage(array $update): \Generator
    {
        $this->callForkDefer(function () {
            yield $this->sleep(1.0);
            yield $this->messages->sendMessage(...);
        });
        yield $this->messages->sendMessage(...);
    }
}
```

After:

```php
use Revolt\EventLoop;
use Amp\delay;

class MyEventHandler {
    public function onUpdateNewMessage(array $update): void
    {
        EventLoop::queue(function () {
            delay(1.0);
            $this->messages->sendMessage(...);
        });
        $this->messages->sendMessage(...);
    }
}
```

Before:

```php
$API = new \danog\MadelineProto\API('session.madeline');
$API->async(true);
$API->loop(function () use ($API) {
    yield $API->messages->sendMessage();
});
```

After:

```php
$API = new \danog\MadelineProto\API('session.madeline');
$API->messages->sendMessage();
```


## Loop API

The `danog/loop` library was refactored, making it much more stable, and fixing some coroutine leaks which may have occurred in certain conditions.  

All loop classes were moved to the `danog\Loop` namespace, and the API now works with seconds instead of milliseconds.

Before:

```php
use \danog\Loop\Generic\GenericLoop;

class ZeusHandler extends EventHandler
{
    public function genLoop()
    {
        yield $this->account->updateStatus([
            'offline' => false
        ]);
        return 20 * 1000;
    }
    public function onStart()
    {
        $genLoop = new GenericLoop([$this, 'genLoop'], 'update Status');
        $genLoop->start();
    }
}
```

After:

```php
use \danog\Loop\GenericLoop;

class ZeusHandler extends EventHandler
{
    public function genLoop(): ?float
    {
        $this->account->updateStatus([
            'offline' => false
        ]);
        return 20.0;
    }
    public function onStart()
    {
        $genLoop = new GenericLoop($this->genLoop(...), 'update Status');
        $genLoop->start();
    }
}
```


## Event handler

- Removed the long-deprecated `setEventHandler` and `$MadelineProto->startAndLoop` methods, you should use `MyEventHandler::startAndLoop`, instead.
- Removed support for the deprecated onLoop method.

Most importantly, the `EventHandler` class was deprecated, please use the `SimpleEventHandler` class now.  

The `SimpleEventHandler` class still supports the legacy `onUpdatexxx` event handler methods, however starting from v8 **they are not covered by the backwards compatibility promise anymore**.  

This means that the structure of updates received in `onUpdatexxx` event handler methods will change at any time, including in minor versions of MadelineProto v8: fields will be removed and changed with only a minor note will be added to the changelog.  

The new [filter-based event API &raquo;](https://docs.madelineproto.xyz/docs/FILTERS.html) should be used instead of `onUpdatexxx` methods: it's much simpler to use, and **is** covered by the backwards compatibility promise, so its fields will **not** change or be removed in minor versions of MadelineProto v8.  


```php
class MyEventHandler extends \danog\MadelineProto\EventHandler {

}

$settings = ['app_info' => ['api_id' => 123456, 'api_hash' => 'xxx']];
$API = new \danog\MadelineProto\API('bot.madeline', $settings);
$API->startAndLoop(MyEventHandler::class);
```

After:

```php
class MyEventHandler extends \danog\MadelineProto\SimpleEventHandler {

}

$settings = (new \danog\MadelineProto\Settings\AppInfo)
    ->setApiId(123456)
    ->setApiHash('xxx');
MyEventHandler::startAndLoop('bot.madeline', $settings);
```

Also, MadelineProto will actively prevent new event handler code from using blocking functions like `file_get_contents`, `file_put_contents`, `curl`: see [here &raquo;](https://docs.madelineproto.xyz/docs/UPDATES.html#automatic-static-analysis) for a more detailed list of async alternatives.

## No more snake_case methods

You can't use `snake_case` variants of MadelineProto methods anymore (deprecated since v5).  

Before:

```php
$info = $API->get_info('danogentili');
$me = $API->get_self();
```

After:


```php
$info = $API->getInfo('danogentili');
$me = $API->getSelf();
```

## Full breaking changelog

- [BC] REMOVED: the long-deprecated `setEventHandler` method, you should use `MyEventHandler::startAndLoop`, instead.
- [BC] REMOVED: the deprecated $MadelineProto->startAndLoop method. Please use MyEventHandler::startAndLoop instead, remove any new \danog\MadelineProto\API line you have in your code if you're using only the event handler.
- [BC] REMOVED: support for the deprecated onLoop method.
- [BC] REMOVED: the setCallback update handling method, please use the event handler with onAny instead.
- [BC] REMOVED: Promise wrapper types from return types everywhere.
- [BC] REMOVED: Removed the legacy MadelineProto Loop APIs, the new github.com/danog/loop APIs do not support generators anymore.
- [BC] REMOVED: Removed support for the long-deprecated snake_case methods, now only camelCase is supported (get_info will not work, only getInfo; and so on).
- [BC] REMOVED: Method danog\MadelineProto\VoIP#whenCreated() was removed
- [BC] REMOVED: Method danog\MadelineProto\StrTools::methodEscape() was removed
- [BC] REMOVED: Method danog\MadelineProto\StrTools::typeEscape() was removed
- [BC] REMOVED: Method danog\MadelineProto\Tools::after() was removed
- [BC] REMOVED: Method danog\MadelineProto\Tools::all() was removed
- [BC] REMOVED: Method danog\MadelineProto\Tools::any() was removed
- [BC] REMOVED: Method danog\MadelineProto\Tools::callForkDefer() was removed
- [BC] REMOVED: Method danog\MadelineProto\Tools::call() was removed
- [BC] REMOVED: Method danog\MadelineProto\Tools::first() was removed
- [BC] REMOVED: Method danog\MadelineProto\Tools::getVar() was removed
- [BC] REMOVED: Method danog\MadelineProto\Tools::hasVar() was removed
- [BC] REMOVED: Method danog\MadelineProto\Tools::setVar() was removed
- [BC] REMOVED: Method danog\MadelineProto\Tools::some() was removed
- [BC] REMOVED: Method danog\MadelineProto\Tools::timeout() was removed
- [BC] REMOVED: Method danog\MadelineProto\Tools::timeoutWithDefault() was removed
- [BC] REMOVED: Method danog\MadelineProto\Tools::wait() was removed
- [BC] REMOVED: Method danog\MadelineProto\Wrappers\Events#setEventHandler() was removed
- [BC] REMOVED: Method danog\MadelineProto\Wrappers\Loop#loopFork() was removed
- [BC] REMOVED: Method danog\MadelineProto\Wrappers\Loop#loop() was removed
- [BC] CHANGED: the isSupergroup, toSupergroup, fromSupergroup methods to a DialogId class, which also has many other useful methods to work with bot API IDs.
- [BC] CHANGED: All download methods except for downloadToFile and downloadToDir now return null instead of true.
- [BC] CHANGED: All `danog\MadelineProto\VoIP` constants were replaced with the `danog\MadelineProto\VoIP\CallState`, `danog\MadelineProto\VoIP\VoIPState` enums.
- [BC] CHANGED: The `danog\MadelineProto\VoIP` class was completely refactored, check out the [new API](docs.madelineproto.xyz/PHP/danog/MadelineProto/VoIP.html) for more info.
- [BC] CHANGED: ORM properties can directly be iterated upon in a foreach without using getIterator (which will not return an amphp iterator anymore). 
- [BC] CHANGED: Finalized a lot of classes that were mistakenly not marked as final.
- [BC] CHANGED: Made some internal details fully private.
- [BC] CHANGED: The session is now contained in a directory, instead of separate files.
- [BC] CHANGED: Automatic API ID fetching via the my.telegram.org wrapper was temporarily removed due to possible IP bans on webhosts.
- [BC] CHANGED: onStart now blocks all updates until it finishes executing. Use the amphp async primitives to start long-running processes in onStart like starting a webserver.
- [BC] CHANGED: You can't assign arbitrary properties to an API instance anymore.
- [BC] CHANGED: Switched to a custom markdown parser with bot API [MarkdownV2](https://core.telegram.org/bots/api#markdownv2-style) syntax, which differs from the previous Markdown syntax supported by parsedown.
- [BC] CHANGED: Markdown text can't contain HTML anymore.
- [BC] CHANGED: danog\MadelineProto\StrTools::methodEscape() was marked "@internal"
- [BC] CHANGED: danog\MadelineProto\StrTools::typeEscape() was marked "@internal"
- [BC] CHANGED: danog\MadelineProto\Tools::getVar() was marked "@internal"
- [BC] CHANGED: danog\MadelineProto\Tools::setVar() was marked "@internal"
- [BC] CHANGED: Parameter 0 of danog\MadelineProto\Tools::callFork() changed name from promise to callable
- [BC] CHANGED: Parameter 0 of danog\MadelineProto\Tools::genVectorHash() changed name from ints to longs
- [BC] CHANGED: Parameter 1 of danog\MadelineProto\Tools::callFork() changed name from actual to args
- [BC] CHANGED: The parameter $token of danog\MadelineProto\Tools::flock() changed from Amp\Promise|null to Amp\Cancellation|null
- [BC] CHANGED: The parameter $token of danog\MadelineProto\Tools::flock() changed from Amp\Promise|null to a non-contravariant Amp\Cancellation|null
- [BC] CHANGED: The return type of danog\MadelineProto\Tools::callFork() changed to Amp\Future
- [BC] CHANGED: The return type of danog\MadelineProto\Tools::echo() changed from Amp\Promise to the non-covariant void
- [BC] CHANGED: The return type of danog\MadelineProto\Tools::echo() changed from Amp\Promise to void
- [BC] CHANGED: The return type of danog\MadelineProto\Tools::flock() changed from Amp\Promise to Closure|null
- [BC] CHANGED: The return type of danog\MadelineProto\Tools::flock() changed from Amp\Promise to the non-covariant Closure|null
- [BC] CHANGED: The return type of danog\MadelineProto\Tools::readLine() changed from Amp\Promise to string
- [BC] CHANGED: The return type of danog\MadelineProto\Tools::readLine() changed from Amp\Promise to the non-covariant string
- [BC] CHANGED: The return type of danog\MadelineProto\Tools::sleep() changed from Amp\Promise to the non-covariant void
- [BC] CHANGED: The return type of danog\MadelineProto\Tools::sleep() changed from Amp\Promise to void
- [BC] CHANGED: The return type of danog\MadelineProto\Wrappers\Events#getEventHandler() changed from danog\MadelineProto\EventHandler to danog\MadelineProto\EventHandler|danog\MadelineProto\Ipc\EventHandlerProxy|__PHP_Incomplete_Class|null
- [BC] CHANGED: The return type of danog\MadelineProto\Wrappers\Events#getEventHandler() changed from danog\MadelineProto\EventHandler to the non-covariant danog\MadelineProto\EventHandler|danog\MadelineProto\Ipc\EventHandlerProxy|__PHP_Incomplete_Class|null

<a href="https://docs.madelineproto.xyz/docs/USING_METHODS.html">Next section</a>