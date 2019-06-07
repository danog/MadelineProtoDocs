---
title: Handling updates (new messages)
description: Update handling can be done in different ways: 
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Handling updates (new messages)

Update handling can be done in different ways: 

* [Self-restart on webhosts](#self-restart-on-webhosts)
* [Async Event driven](#async-event-driven)
* [Multi-account: Async Combined Event driven update handling](#async-combined-event-driven)
* [Async Callback](#async-callback)
* [Noop (default)](#noop)
* [Fetch all updates from the beginning](#fetch-all-updates-from-the-beginning)


## Self-restart on webhosts

When running the `loop()` method via web, MadelineProto will automatically enable a **magical self-restart hack**, to keep the bot running even on webhosts with limited execution time.  

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
class EventHandler extends \danog\MadelineProto\EventHandler
{
    public function __construct($MadelineProto)
    {
        parent::__construct($MadelineProto);
    }
    public function onAny($update)
    {
        \danog\MadelineProto\Logger::log("Received an update of type ".$update['_']);
    }
    public function onUpdateNewChannelMessage($update)
    {
        yield $this->onUpdateNewMessage($update);
    }
    public function onUpdateNewMessage($update)
    {
        if (isset($update['message']['out']) && $update['message']['out']) {
            return;
        }
        $res = json_encode($update, JSON_PRETTY_PRINT);
        if ($res == '') {
            $res = var_export($update, true);
        }

        try {
            yield $this->messages->sendMessage(['peer' => $update, 'message' => $res, 'reply_to_msg_id' => $update['message']['id']]);
        } catch (\danog\MadelineProto\RPCErrorException $e) {
            yield $this->messages->sendMessage(['peer' => '@danogentili', 'message' => $e]);
        }

        try {
            if (isset($update['message']['media']) && ($update['message']['media']['_'] == 'messageMediaPhoto' || $update['message']['media']['_'] == 'messageMediaDocument')) {
                $time = microtime(true);
                $file = yield $this->download_to_dir($update, '/tmp');
                yield $this->messages->sendMessage(['peer' => $update, 'message' => 'Downloaded to '.$file.' in '.(microtime(true) - $time).' seconds', 'reply_to_msg_id' => $update['message']['id']]);
            }
        } catch (\danog\MadelineProto\RPCErrorException $e) {
            yield $this->messages->sendMessage(['peer' => '@danogentili', 'message' => $e]);
        }
    }
}


$MadelineProto = new \danog\MadelineProto\API('bot.madeline');
$MadelineProto->async(true);
$MadelineProto->loop(function () use ($MadelineProto) {
    yield $MadelineProto->start();
    yield $MadelineProto->setEventHandler('\EventHandler');
});
$MadelineProto->loop();
```

This will create an event handler class `EventHandler`, create a MadelineProto session, and set the event handler class to our newly created event handler.

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

To break out of the loop just call `die();`, or throw an exception from within (make sure to catch it outside, in the `$MadelineProto->loop()` call).  


## Async Combined event driven

```php
class EventHandler extends \danog\MadelineProto\CombinedEventHandler
{
    public function __construct($CombinedMadelineProto)
    {
        parent::__construct($CombinedMadelineProto);
    }
    public function onAny($update, $session)
    {
        \danog\MadelineProto\Logger::log("Received an update of type ".$update['_']);
    }
    public function onLoop()
    {
        \danog\MadelineProto\Logger::log("Working...");
    }
    public function onUpdateNewChannelMessage($update, $session)
    {
        yield $this->onUpdateNewMessage($update, $session);
    }
    public function onUpdateNewMessage($update, $session)
    {
        if (isset($update['message']['out']) && $update['message']['out']) {
            return;
        }
        $res = json_encode($update, JSON_PRETTY_PRINT);
        if ($res == '') {
            $res = var_export($update, true);
        }

        try {
            yield $this->{$session}->messages->sendMessage(['peer' => $update, 'message' => $res, 'reply_to_msg_id' => $update['message']['id']]);
        } catch (\danog\MadelineProto\RPCErrorException $e) {
            yield $this->{$session}->messages->sendMessage(['peer' => '@danogentili', 'message' => $e]);
        }

        try {
            if (isset($update['message']['media']) && ($update['message']['media']['_'] == 'messageMediaPhoto' || $update['message']['media']['_'] == 'messageMediaDocument')) {
                $time = microtime(true);
                $file = yield $this->{$session}->download_to_dir($update, '/tmp');
                yield $this->{$session}->messages->sendMessage(['peer' => $update, 'message' => 'Downloaded to '.$file.' in '.(microtime(true) - $time).' seconds', 'reply_to_msg_id' => $update['message']['id']]);
            }
        } catch (\danog\MadelineProto\RPCErrorException $e) {
            yield $this->{$session}->messages->sendMessage(['peer' => '@danogentili', 'message' => $e]);
        }
    }
}

$settings = [];
$CombinedMadelineProto = new \danog\MadelineProto\CombinedAPI('combined_session.madeline', ['bot.madeline' => $settings, 'user.madeline' => $settings, 'user2.madeline' => $settings]);
$CombinedMadelineProto->async(true);
$CombinedMadelineProto->loop(function () use ($CombinedMadelineProto) {
    $res = [];
    foreach ([
        'bot.madeline' => 'Bot Login',
        'user.madeline' => 'Userbot login',
        'user2.madeline' => 'Userbot login (2)'
    ] as $session => $message) {
        \danog\MadelineProto\Logger::log($message, \danog\MadelineProto\Logger::WARNING);
        $res []= $CombinedMadelineProto->instances[$session]->start();
    }
    yield $CombinedMadelineProto->all($res);
    yield $CombinedMadelineProto->setEventHandler('\EventHandler');
}
$CombinedMadelineProto->loop();
```

This will create an event handler class `EventHandler`, create a **combined** MadelineProto session with session files `bot.madeline`, `user.madeline`, `user2.madeline`, and set the event handler class to our newly created event handler.

This yield syntax might be new to you, even if you already used MadelineProto in the past.  
It's a new syntax to allow async **parallel processing** of updates and HUGE speed improvements.  
It was recently introduced in MadelineProto, [here's a full explanation](ASYNC.html).  
If your code still relies on the old synchronous behaviour, it's still supported, but I HIGHLY recommend you switch to the new async syntax: it's __super__ easy, [just add a `yield` in front of method calls](ASYNC.html)!  

When an [Update](https://docs.madelineproto.xyz/API_docs/types/Update.html) is received, the corresponding `onUpdateType` event handler method is called. 

To get a list of all possible update types, [click here](https://docs.madelineproto.xyz/API_docs/types/Update.html).  

If such a method does not exist, the `onAny` event handler method is called.  
If the `onAny` event handler method does not exist, the update is ignored.  
The first paramter of the event handler method will always be the [Update](https://docs.madelineproto.xyz/API_docs/types/Update.html), the second parameter will always be the **session name**.


The `onLoop` method is not recommended anymore, use AMPHP's [repeat](https://amphp.org/amp/event-loop/api#repeat) or MadelineProto's [async loop API](ASYNC.html#async-loop-apis) to schedule actions in a cron-like manner.  

To access the `$MadelineProto` instance of the account that sent the update, from inside of the event handler, simply access `$this->{$session_name}` (`$session_name` is the second parameter value of the event handler method, or just the session filename):
```php
$this->{$session_name}->messages->sendMessage(['peer' => '@danogentili', 'message' => 'hi']);
$this->{'user2.madeline'}->messages->sendMessage(['peer' => '@danogentili', 'message' => 'hi2']);
```

If you intend to use your own constructor in the event handler, make sure to call the parent construtor with the only parameter provided to your constructor.

If you need to use the [__sleep](https://www.php.net/manual/en/language.oop5.magic.php#object.sleep) function, make sure it is called `__magic_sleep`, instead.  

The update handling loop is started by the `$MadelineProto->loop()` method, and it will automatically restart the script if execution time runs out.

To break out of the loop just call `die();`, or throw an exception from within (make sure to catch it outside, in the `$MadelineProto->loop()` call).  



## Async callback

```php
$MadelineProto = new \danog\MadelineProto\API('bot.madeline');

$MadelineProto->start();
$MadelineProto->setCallback(function ($update) use ($MadelineProto) {

    if (isset($update['message']['out']) && $update['message']['out']) {
        return;
    }
    $res = json_encode($update, JSON_PRETTY_PRINT);
    if ($res == '') {
        $res = var_export($update, true);
    }

    try {
        yield $MadelineProto->messages->sendMessage(['peer' => $update, 'message' => $res, 'reply_to_msg_id' => $update['message']['id']]);
    } catch (\danog\MadelineProto\RPCErrorException $e) {
        yield $MadelineProto->messages->sendMessage(['peer' => '@danogentili', 'message' => $e]);
    }
});
$MadelineProto->async(true);
$MadelineProto->loop();
```
When an [Update](https://docs.madelineproto.xyz/API_docs/types/Update.html) is received, the provided callback function is called.

The update handling loop is started by the `$MadelineProto->loop()` method, and it will automatically restart the script if execution time runs out.  

This yield syntax might be new to you, even if you already used MadelineProto in the past.  
It's a new syntax to allow async **parallel processing** of updates and HUGE speed improvements.  
It was recently introduced in MadelineProto, [here's a full explanation](ASYNC.html).  
If your code still relies on the old synchronous behaviour, it's still supported, but I HIGHLY recommend you switch to the new async syntax: it's __super__ easy, [just add a `yield` in front of method calls](ASYNC.html)!  

To break out of the loop just call `die();`, or throw an exception from within (make sure to catch it outside, in the `$MadelineProto->loop()` call).  



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
