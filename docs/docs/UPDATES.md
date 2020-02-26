---
title: Handling updates (new messages)
description: Update handling can be done in different ways: 
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Handling updates (new messages)

Update handling can be done in different ways: 

* [Self-restart on webhosts](#self-restart-on-webhosts)
* [Async Event driven](#async-event-driven)
* [Multi-account: Async Event driven](#async-event-driven)
* [Async Callback](#async-callback)
* [Noop (default)](#noop)
* [Fetch all updates from the beginning](#fetch-all-updates-from-the-beginning)


## Self-restart on webhosts

When running the `loop()` method via web, MadelineProto will automatically enable a **magical self-restart hack** (callback ID `restarter`), to keep the bot running even on webhosts with limited execution time.  

Locking will also be handled automatically (as well as disconnection from the user that opened the page), so even if you start the script via web several times, only one instance will be running at a time (no need to do flocking manually!).  

It relies on the shutdown function, so you must not set a custom shutdown function in your code, and instead use the **MadelineProto shutdown static API**:  

```php
use danog\MadelineProto\Shutdown;

$id = Shutdown::addCallback(static function () {
    // This function will run on shutdown
});

$id = Shutdown::addCallback(static function () {
    // This function will run on shutdown
}, 'custom id');

$id = Shutdown::addCallback(static function () {
    // This function will overwrite the previously set function with custom id
}, 'custom id');

$ok = Shutdown::removeCallback($id);
```

You can of course pass non-static functions, any type of callable is accepted.  
A second optional parameter can also be accepted, containing the ID of the callable: you can use this if you want to later overwrite the callable with another callback, or remove it altogether.  

The `removeCallback` will return true if the callback exists and it was removed correctly, false otherwise (as with all new MadelineProto 4.0 APIs, there are PHPDOCs for these methods so you'll see them in your IDE).


## Async Event driven

```php
use danog\MadelineProto\EventHandler;
use danog\MadelineProto\Tools;
use danog\MadelineProto\API;
use danog\MadelineProto\Logger;
use danog\MadelineProto\RPCErrorException;

/**
 * Event handler class.
 */
class MyEventHandler extends EventHandler
{
    /**
     * @var int|string Username or ID of bot admin
     */
    const ADMIN = "danogentili"; // Change this
    /**
     * Get peer(s) where to report errors
     *
     * @return int|string|array
     */
    public function getReportPeers()
    {
        return [self::ADMIN];
    }
    /**
     * Handle updates from supergroups and channels
     *
     * @param array $update Update
     * 
     * @return void
     */
    public function onUpdateNewChannelMessage(array $update): \Generator
    {
        return $this->onUpdateNewMessage($update);
    }
    /**
     * Handle updates from users.
     *
     * @param array $update Update
     *
     * @return \Generator
     */
    public function onUpdateNewMessage(array $update): \Generator
    {
        if ($update['message']['_'] === 'messageEmpty' || $update['message']['out'] ?? false) {
            return;
        }
        $res = \json_encode($update, JSON_PRETTY_PRINT);

        try {
            yield $this->messages->sendMessage(['peer' => $update, 'message' => "<code>$res</code>", 'reply_to_msg_id' => isset($update['message']['id']) ? $update['message']['id'] : null, 'parse_mode' => 'HTML']);
            if (isset($update['message']['media']) && $update['message']['media']['_'] !== 'messageMediaGame') {
                yield $this->messages->sendMedia(['peer' => $update, 'message' => $update['message']['message'], 'media' => $update]);
            }
        } catch (RPCErrorException $e) {
            $this->report("Surfaced: $e");
        } catch (Exception $e) {
            if (\stripos($e->getMessage(), 'invalid constructor given') === false) {
                $this->report("Surfaced: $e");
            }
        }
    }
}
$settings = [
    'logger' => [
        'logger_level' => 5
    ],
    'serialization' => [
        'serialization_interval' => 30,
    ],
];

$MadelineProto = new API('bot.madeline', $settings);
$MadelineProto->startAndLoop(MyEventHandler::class);
```

This will create an event handler class `MyEventHandler`, create a MadelineProto session, and set the event handler class to our newly created event handler.

The **new** `startAndLoop` method automatically initializes MadelineProto, **enables async**, logs in the user/bot, initializes error reporting, catches and reports all errors surfacing from the event loop to the peers returned by the `getReportPeers` method.

This yield syntax might be new to you, even if you already used MadelineProto in the past.  
It's a new syntax to allow async **parallel processing** of updates and HUGE speed improvements.  
It was recently introduced in MadelineProto, [here's a full explanation](ASYNC.html).  
If your code still relies on the old synchronous behaviour, it's still supported, but I HIGHLY recommend you switch to the new async syntax: it's __super__ easy, [just add a `yield` in front of method calls](ASYNC.html)!  

When an [Update](https://docs.madelineproto.xyz/API_docs/types/Update.html) is received, the corresponding `onUpdateType` event handler method is called.  

To get a list of all possible update types, [click here](https://docs.madelineproto.xyz/API_docs/types/Update.html). 

If such a method does not exist, the `onAny` event handler method is called.  
If the `onAny` event handler method does not exist, the update is ignored.  
The `onLoop` method is not recommended anymore, use AMPHP's [repeat](https://amphp.org/amp/event-loop/api#repeat) or MadelineProto's [async loop API](ASYNC.html#async-loop-apis) to schedule actions in a cron-like manner.  

To access the `$MadelineProto` instance inside of the event handler, simply access `$this`:
```php
$this->messages->sendMessage(['peer' => '@danogentili', 'message' => 'hi']);
```

If you intend to use your own constructor in the event handler, make sure to call the parent construtor with the only parameter provided to your constructor.

The update handling loop is started by the `$MadelineProto->loop()` method, and it will automatically restart the script if execution time runs out.

To forecfully restart and apply changes made to the event handler class, call `$MadelineProto->restart();`.  


## Async event driven (multiaccount)

```php
use danog\MadelineProto\EventHandler;
use danog\MadelineProto\Tools;
use danog\MadelineProto\API;
use danog\MadelineProto\Logger;
use danog\MadelineProto\RPCErrorException;

// Normal event handler definition as above

$MadelineProtos = [];
foreach ([
    'bot.madeline' => 'Bot Login',
    'user.madeline' => 'Userbot login',
    'user2.madeline' => 'Userbot login (2)'
] as $session => $message) {
    Logger::log($message, Logger::WARNING);
    $MadelineProtos []= (new API($session))->startAndLoopBackground(MyEventHandler::class);
}

Tools::wait(Tools::all($MadelineProtos));
```

This will create an event handler class `EventHandler`, create a **combined** MadelineProto session with session files `bot.madeline`, `user.madeline`, `user2.madeline`, and set the event handler class to our newly created event handler.

Usage is the same as for [the normal event handler](#async-event-driven), with the difference that by using `loopFork`, multiple accounts can receive and handle updates in parallel, each with its own event handler instance.

## Noop

```php
$MadelineProto = new \danog\MadelineProto\API('bot.madeline');

$MadelineProto->start();
$MadelineProto->setNoop();
```
When an [Update](https://docs.madelineproto.xyz/API_docs/types/Update.html) is received, nothing is done. This is useful if you need to populate the internal peer database with peers to avoid `This peer is not present in the internal peer database errors`, but don't need to handle updates.  
This is the default.  


## Fetch all updates from the beginning

You can use the `resetUpdateState` method to reset the update state and fetch all updates from the beginning:  
```php
$MadelineProto->resetUpdateState();
```

<a href="https://docs.madelineproto.xyz/docs/SETTINGS.html">Next section</a>