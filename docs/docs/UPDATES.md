---
title: "Handling updates (new messages)"
description: "Update handling can be done in different ways: "
nav_order: 9
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Handling updates (new messages)

Update handling can be done in different ways: 

* [Self-restart on webhosts](#self-restart-on-webhosts)
* [Async Event driven](#async-event-driven)
  * [Built-in database driver](#built-in-database-driver)
* [Async Event driven multi-account](#async-event-driven-multiaccount)
* [Noop (default)](#noop)


## Self-restart on webhosts

When running the event handler via web, MadelineProto will automatically enable a **magical self-restart hack** (callback ID `restarter`), to keep the bot running even on webhosts with limited execution time.  

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

The `removeCallback` will return true if the callback exists and it was removed correctly, false otherwise (as with all new MadelineProto APIs, there are PHPDOCs for these methods so you'll see them in your IDE).


## Async Event driven

```php
use danog\MadelineProto\EventHandler;
use danog\MadelineProto\Tools;
use danog\MadelineProto\API;
use danog\MadelineProto\Logger;
use danog\MadelineProto\Settings;
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
     * List of properties automatically stored in database (MySQL, Postgres, redis or memory).
     * @see https://docs.madelineproto.xyz/docs/DATABASE.html
     * @var array
     */
    protected static array $dbProperties = [
        'dataStoredOnDb' => 'array'
    ];

    /**
     * @var DbArray<array>
     */
    protected $dataStoredOnDb;

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
      * Called on startup, can contain async calls for initialization of the bot
      *
      * @return void
      */
    public function onStart()
    {
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

        yield $this->messages->sendMessage(['peer' => $update, 'message' => "<code>$res</code>", 'reply_to_msg_id' => isset($update['message']['id']) ? $update['message']['id'] : null, 'parse_mode' => 'HTML']);
        if (isset($update['message']['media']) && $update['message']['media']['_'] !== 'messageMediaGame') {
            yield $this->messages->sendMedia(['peer' => $update, 'message' => $update['message']['message'], 'media' => $update]);
        }

        // You can also use the built-in MadelineProto MySQL async driver!

        // Can be anything serializable, an array, an int, an object
        $myData = [];

        // Use the isset method to check whether some data exists in the database
        if (yield $this->dataStoredOnDb->isset('yourKey')) {
            // Always yield when fetching data
            $myData = yield $this->dataStoredOnDb['yourKey'];
        }
        $this->dataStoredOnDb['yourKey'] = $myData + ['moreStuff' => 'yay'];

        $this->dataStoredOnDb['otherKey'] = 0;
        unset($this->dataStoredOnDb['otherKey']);

        $this->logger("Count: ".(yield $this->dataStoredOnDb->count()));

        // You can even use an async iterator to iterate over the data
        $iterator = $this->dataStoredOnDb->getIterator();
        while (yield $iterator->advance()) {
            [$key, $value] = $iterator->getCurrent();
            $this->logger($key);
            $this->logger($value);
        }
    }
}

$settings = new Settings;
$settings->getLogger()->setLevel(Logger::LEVEL_ULTRA_VERBOSE);

MyEventHandler::startAndLoop('bot.madeline', $settings);
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

To forecfully restart and apply changes made to the event handler class, call `$MadelineProto->restart();`.  

### Built-in database driver

You can also directly connect to any database using the same [async MySQL/Postgres/Redis ORM](DATABASE.html) used by MadelineProto internally.  

To do so, simply [specify the database settings](DATABASE.html), and declare a static `$dbProperties` property to initialize the async database mapper:  
```php
class MyEventHandler extends EventHandler
{
    /**
     * List of properties automatically stored in database (MySQL, Postgres, redis or memory).
     * @see https://docs.madelineproto.xyz/docs/DATABASE.html
     * @var array
     */
    protected static array $dbProperties = [
        'dataStoredOnDb' => 'array'
    ];

    /**
     * @var DbArray<array>
     */
    protected $dataStoredOnDb;

    // ...
```

And use the newly created `$dataStoredOnDb` property to access the database:  
```php
// Can be anything serializable, an array, an int, an object
$myData = [];

// Use the isset method to check whether some data exists in the database
if (yield $this->dataStoredOnDb->isset('yourKey')) {
    // Always yield when fetching data
    $myData = yield $this->dataStoredOnDb['yourKey'];
}
$this->dataStoredOnDb['yourKey'] = $myData + ['moreStuff' => 'yay'];

$this->dataStoredOnDb['otherKey'] = 0;
unset($this->dataStoredOnDb['otherKey']);

$this->logger("Count: ".(yield $this->dataStoredOnDb->count()));

// You can even use an async iterator to iterate over the data!
$iterator = $this->dataStoredOnDb->getIterator();
while (yield $iterator->advance()) {
    [$key, $value] = $iterator->getCurrent();
    $this->logger($key);
    $this->logger($value);
}
```

The returned iterator is an async [Amp iterator](https://amphp.org/amp/iterators/#iterator-consumption), that yields an array with the key, followed by the value.  
[Psalm](https://psalm.dev) generics typing is supported.  

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
    $MadelineProtos []= new API($session);
}

API::startAndLoopMulti($MadelineProtos, MyEventHandler::class);
```

This will create an event handler class `EventHandler`, create a **combined** MadelineProto session with session files `bot.madeline`, `user.madeline`, `user2.madeline`, and set the event handler class to our newly created event handler.

Usage is the same as for [the normal event handler](#async-event-driven), with the difference is that multiple accounts can receive and handle updates in parallel, each with its own event handler instance.

## Noop

```php
$MadelineProto = new \danog\MadelineProto\API('bot.madeline');

$MadelineProto->start();
$MadelineProto->setNoop();
```
When an [Update](https://docs.madelineproto.xyz/API_docs/types/Update.html) is received, nothing is done. This is useful if you need to populate the internal peer database with peers to avoid `This peer is not present in the internal peer database errors`, but don't need to handle updates.  
This is the default.  

<a href="https://docs.madelineproto.xyz/docs/DATABASE.html">Next section</a>