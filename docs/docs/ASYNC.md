---
title: Async
description: MadelineProto now features async, for **incredible speed improvements**, and parallel processing.  
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Async

MadelineProto now features async, for **incredible speed improvements**, and parallel processing.  
Powered by [amphp](https://amphp.org), MadelineProto wraps the AMPHP APIs to provide a simpler generator-based async API.  

* [Usage](#usage)
  * [Loading the latest version of MadelineProto](#loading-the-latest-version-of-madelineproto)
  * [Enabling the MadelineProto async API](#enabling-the-madelineproto-async-api)
  * [Using the MadelineProto async API](#using-the-madelineproto-async-api)
    * [Async in event handler](#async-in-event-handler)
    * [Async in callback handler](#async-in-callback-handler)
    * [Wrapped async](#wrapped-async)
    * [Ignored async](#ignored-async)
    * [Blocking async](#blocking-async)
  * [MadelineProto and AMPHP async APIs](#madelineproto-and-amphp-async-apis)
    * [Helper methods](#helper-methods)
      * [Async sleep](#async-sleep-does-not-block-the-main-thread)
      * [MadelineProto artax HTTP client](#madelineproto-artax-http-client)
      * [Async forking](#async-forking-does-single-thread-forking)
      * [Combining async operations](#combining-async-operations)
    * [MadelineProto async loop APIs](#async-loop-apis)
      * [Loop](#loop)
      * [ResumableLoop](#resumableloop)
      * [SignalLoop](#signalloop)
      * [ResumableSignalLoop](#resumablesignalloop)
      * [GenericLoop](#genericloop)

## Usage

What exactly __is__ **async**, you may ask, and how is it better than **threading** or **multiprocessing**?  
Async is a relatively new programming pattern that allows you to easily write **non-blocking** code **as if you were using standard** blocking functions, all without the need for complex message exchange systems and synchronization handling for threaded programs, that only add overhead and complexity to your programs, making everything slower and error-prone.  

That's very cool and all, you might think, but how exactly does this __async__ stuff work? Well, as it turns out, it's very easy.  

Instead of writing code like this:  
```php
$file = $MadelineProto->download_to_dir($bigfile, '/tmp/');
```

Write it like **this**:  
```php
$file = yield $MadelineProto->download_to_dir($bigfile, '/tmp/');
```

### That's it.

It's really **that** easy, you just have to add a `yield` before calling MadelineProto methods.  
The `yield` will automatically **suspend** the execution of the function, letting the program do other stuff while the file is being downloaded.  
Once the file is downloaded, execution is automatically **resumed** from that exact point in the function.  

This means that you can handle multiple updates, download/upload multiple files all together in one process, as if you were writing normal synchronous code + making everything a lot faster.  

If your code still relies on the old synchronous behaviour, don't worry, there is backward compatibility.  
However, I highly recommend you switch to async, due to the huge performance and parallelism benefits.  

## Loading the latest version of MadelineProto

In order to use the `yield` operator in MadelineProto, you have to load the **latest version** of MadelineProto from the **master** branch (alpha) by loading it through composer (`dev-master`) or with madeline.php:  
```php
<?php

if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';
```

The `MADELINE_BRANCH` constant you defines which branch of MadelineProto madeline.php should load.  
When the constant is not set, the `old` stable branch is loaded; if the value is an empty string, the `master` branch is loaded; otherwise, the selected branch name is loaded.  
**WARNING**: MadelineProto async is not compatible with pthreads or pcntl, so please uninstall pthreads and do not use `pcntl_fork` in your bot.  

## Enabling the MadelineProto async API

The `yield` operator can only be used within functions, once MadelineProto's async mode is enabled.  
To do that, simply run the `async` function, or pass the async enabler flag separately to each method call, if you want to make only some calls async.  

This will enable async mode for **all** MadelineProto functions:  
```php
$MadelineProto->async(true);
// ...
yield $MadelineProto->messages->sendMessage(...);
```

This will enable async mode for **only one** specific call of a MadelineProto function (by adding a **new** array parameter after all the required parameters):  
```php
yield $MadelineProto->messages->sendMessage(..., ['async' => true]);
```

## Using the MadelineProto async API

As mentioned earlier, you can only use the `yield` operator within functions, but not just any function, for example (**WILL NOT WORK**):
```php
$sm = function ($chatID, $message) use ($MadelineProto) {
    $id = (yield $MadelineProto->get_info($chatID, ['async' => true]))['bot_api_id'];
    $res = yield $MadelineProto->messages->sendMesssage(['peer' => $chatID, 'message' => "Message from: $id\n$message"], ['async' => true]);
    return $res;
};
$result = $sm('@danogentili', 'hi');
```

This **will not work**, because the result of a function that uses `yield` is not the `return`ed value, but a [generator](https://www.php.net/manual/en/language.generators.overview.php), which is what the async AMPHP API is based on.  
If the generator is not __passed to the AMPHP event loop__, execution of the function will not be resumed: when MadelineProto asynchronously obtains the result of the get_info, execution of the function is never resumed, and the line with sendMessage is never called.  
To avoid this problem, only call asynchronous functions in the event/callback update handler, or in functions called by the event/callback update handler, or inside a function passed to loop.  
You can also call asynchronous functions created by you, within other asynchronous functions.  
Generators in MadelineProto are equivalent to promises, which is a paradigm you may have used in other languages.

### Async in [event handler](https://docs.madelineproto.xyz/docs/UPDATES.html#event-driven):
```php
$MadelineProto->async(true);
class EventHandler extends \danog\MadelineProto\EventHandler
{
    public function onAny($update)
    {
        if (isset($update['message']['out']) && $update['message']['out']) {
            return;
        }
        if (isset($update['message']['media']) && $update['message']['media']['_'] !== 'messageMediaGame') {
            yield $this->download_to_dir($update, '/tmp');
            yield $this->messages->sendMedia(['peer' => $update, 'message' => $update['message']['message'], 'media' => $update]);
        }

        $res = json_encode($update, JSON_PRETTY_PRINT);

        yield $this->sleep(3);

        try {
            yield $this->sm($update, "<code>$res</code>\nAsynchronously, after 3 seconds");
        } catch (\danog\MadelineProto\RPCErrorException $e) {
            \danog\MadelineProto\Logger::log((string) $e, \danog\MadelineProto\Logger::FATAL_ERROR);
        } catch (\danog\MadelineProto\Exception $e) {
            \danog\MadelineProto\Logger::log((string) $e, \danog\MadelineProto\Logger::FATAL_ERROR);
        }
    }
    public function sm($peer, $message)
    {
        yield $this->messages->sendMessage(['peer' => $peer, 'message' => $message, 'reply_to_msg_id' => isset($update['message']['id']) ? $update['message']['id'] : null, 'parse_mode' => 'HTML']);
    }
}
```

### Async in [callback handler](https://docs.madelineproto.xyz/docs/UPDATES.html#callback):
```php
$MadelineProto->async(true);
$MadelineProto->setCallback(function ($update) use ($MadelineProto) {
    if (isset($update['message']['out']) && $update['message']['out']) {
        return;
    }
    yield $MadelineProto->sleep(3);
    yield $MadelineProto->messages->sendMessage(['peer' => $update, 'message' => 'Hi after 3 seconds']);
});
```

### Wrapped async
```php
$MadelineProto->async(true);
$MadelineProto->loop(function () use ($MadelineProto) {
    yield $MadelineProto->messages->sendMessage(['peer' => '@danogentili', 'message' => 'hi']);
    // You can also have an asynchronous get_updates (deprecated) loop in here, if you want to; just don't forget to use yield for all MadelineProto functions.
});
```

### Ignored async
```php
$MadelineProto->messages->sendMessage(['peer' => '@danogentili', 'message' => 'a'], ['async' => true]);
$MadelineProto->messages->sendMessage(['peer' => '@danogentili', 'message' => 'b'], ['async' => true]);
```

You can use the async version of MadelineProto functions **without** yield if you don't want the request to block, and you don't need the result of the function.  
This is allowed, but the order of the function calls will not be guaranteed: you can use [call queues](https://docs.madelineproto.xyz/docs/USING_METHODS.html#queues) if you want to make sure the order of the calls remains the same.
See [async forking](#async-forking-does-async-single-thread-forking).  

### Blocking async
```php
$result = blocking_function();
```

Sometimes, you have to call non-async functions in your code: that is allowed in async MadelineProto, you just have to call your functions normally without `yield`.  
However, you shouldn't do (or need to do) this, because this renders async completely useless.  
AMPHP already provides async versions of curl, `file_get_contents`, MySQL, redis, postgres, and many more native PHP functions: 

## MadelineProto and AMPHP async APIs

MadelineProto and AMPHP both provide a lot of async functions: all of MadelineProto's functions are async, for example; and AMPHP provides [multiple packages](https://amphp.org/packages) to work asynchronously with HTTP requests, websockets, databases (MySQL, redis, postgres, DNS, sockets and [much more](https://github.com/amphp/)!  
When using AMPHP libraries, you just have to use them with yield, no need to start the event loop, as long as you're running the functions inside MadelineProto's update handler/loop.  

Also, you should read the AMPHP docs, especially the [event loop docs](https://amphp.org/amp/event-loop/api): AMPHP provides multiple helper methods for executing actions repeatedly every N seconds in a non-blocking manner, or to defer execution of certain actions (aka async cron).  

### Helper methods

MadelineProto also provides a few generic async helper methods: when possible, always use MadelineProto's wrapped versions of the [amphp combinators](https://amphp.org/amp/promises/combinators) and [amphp helpers](https://amphp.org/amp/promises/miscellaneous) instead of original amphp methods (`all`, `any`, `some`, `first`, ...).  

#### Async sleep (does not block the main thread)
```php
yield $MadelineProto->sleep(3);
```

#### MadelineProto artax HTTP client

When using amphp's [artax](https://amphp.org/artax) to make high-speed asynchronous HTTP requests (downloading files, etc.), use MadelineProto's modified Artax client, instead.  
It automatically supports the socks/HTTP proxies specified in MadelineProto's settings (will use proxies only if the file can't be downloaded normally), and soon DoH for greater security.  

To use MadelineProto's artax client, instead of creating artax's default client:  
```php
$client = new Amp\Artax\DefaultClient;
```

Simply get MadelineProto's artax client:  
```php
$client = $MadelineProto->getHTTPClient();
```

From here it's like in the [artax docs](https://amphp.org/artax).  

#### Async forking (does async single-thread forking)

Useful if you need to start a process in the background and you want throwed exceptions to surface up.  
These exceptions will exit the event loop, turning off the script unless you wrap `$MadelineProto->loop()` with a try-catch.  
Use it when you do not need the result of a method (see [ignored async](#ignored-async)), but you want eventual errors to crash the script.  
Otherwise, just use the method without yield.  

```php
// Exceptions will surface out of the event loop()
$MadelineProto->callFork($MadelineProto->messages->sendMessage([...]));
// Exceptions will be ignored
$MadelineProto->messages->sendMessage([...]);

// Like the first one, but the call will be deferred to the next event loop tick
$MadelineProto->callForkDefer($MadelineProto->messages->sendMessage([...]));
```

Ignoring exceptions is usually not good practice, so it's best to wrap the method you're calling in a closure with a try-catch with some error handling code inside of it, calling it right after that and passing it to callFork:

```php
$MadelineProto->callFork((function () use ($MadelineProto) {
    try {
        $MadelineProto->messages->sendMessage([...])
    } catch (\Exception $e) {
        // Handle by logging and stuff
    }
})());
```

#### Combining async operations

These methods can be used to execute multiple async operations simultaneously and wait for the result of all of them.  
Each method has different error handling techniques, see the [amphp docs](https://amphp.org/amp/promises/combinators).  
Note that if you just take the result of these methods without yielding it, you can use it as a normal promise/generator.  

```
$promise1 = $MadelineProto->messages->sendMessage(...);
$promise2 = $MadelineProto->messages->sendMessage(...);
// $promise3 = ...;

// Equivalent to Amp\Promise\all(), but works with generators, too
$results = yield $MadelineProto->all([$promise1, $promise2, $generator3]);

// Equivalent to Amp\Promise\first(), but works with generators, too
$results = yield $MadelineProto->first([$promise1, $promise2, $generator3]);

// Equivalent to Amp\Promise\any(), but works with generators, too
$results = yield $MadelineProto->any([$promise1, $promise2, $generator3]);

// Equivalent to Amp\Promise\some(), but works with generators, too
$results = yield $MadelineProto->some([$promise1, $promise2, $generator3]);

```

#### Handling timeouts

These methods can be used to wait for a certain amount of time for a result, and then throw an `Amp\TimeoutException` or simply continue execution if no result was obtained.  

```
// Waits for the result for 2 seconds and then throws an \Amp\TimeoutException
$result = yield $MadelineProto->timeout($promise, 2)

// Waits for the result for 2 seconds, returns the result or null (which is the result of sleep())
$result = yield $MadelineProto->first([$promise, $MadelineProto->sleep(2)]);
```

### Async loop APIs

MadelineProto provides a very useful async loop APIs, for executing operations periodically or on demand.  
It's a more flexible and powerful alternative to AMPHP's [repeat](https://amphp.org/amp/event-loop/api#repeat), allowing dynamically changeable repeat periods, resumes and signaling.  
All loop APIs are defined by one or more [interfaces](https://github.com/danog/MadelineProto/tree/master/src/danog/MadelineProto/Loop): however, to use them, you would usually have to extend only one of the [abstract class implementations](https://github.com/danog/MadelineProto/tree/master/src/danog/MadelineProto/Loop/Impl).  

#### Loop

A basic loop, capable of running in background (asynchronously) the code contained in the `loop` function.  

[Interface](https://github.com/danog/MadelineProto/blob/master/src/danog/MadelineProto/Loop/LoopInterface.php):  
```php
namespace danog\MadelineProto\Loop;

interface LoopInterface
{
    /**
     * Start the loop.
     *
     * @return void
     */
    public function start();

    /**
     * The actual loop.
     *
     * @return void
     */
    public function loop();

    /**
     * Get name of the loop
     *
     * @return string
     */
    public function __toString(): string;
}
```

Usually one would extend the [Loop implementation](https://github.com/danog/MadelineProto/blob/master/src/danog/MadelineProto/Loop/Impl/Loop.php).  
The loop function will be run only once, every time the `start` method (already implemented in the abstract Impl class we're extending) is called.  
Multiple calls to `start` will be ignored, logging an error and returning `false` instead of `true`.  
The `__toString` method still has to be implemented in order to get the name of the loop, that will be used by the MadelineProto logging mechanism every time the loop starts/exits/fails to start.  
By default, an instance of MadelineProto MUST be passed to the constructor of the function, or **if** a custom constructor is defined, the `$this->API` property MUST be set to an instance of MadelineProto.  

```php
use danog\MadelineProto\Loop\Impl\Loop;
class MyLoop extends Loop
{
    private $callable;
    public function __construct($API, $callable)
    {
        $this->API = $API;
        $this->callable = $callable;
    }
    public function loop()
    {
        $MadelineProto = $this->API;
        $logger = &$MadelineProto->logger;
        $callable = $this->callable;

        $result = null;
        while (true) {
            $params = yield $callable($result);
            $result = yield $MadelineProto->messages->sendMessage($params);
        }
    }
    public function __toString(): string
    {
        return "my custom loop";
    }
}
```


#### ResumableLoop

A way more useful loop that exposes APIs to pause and resume the execution of the loop, both from outside of the loop, and in a cron-like manner from inside of the loop.  

[Interface](https://github.com/danog/MadelineProto/blob/master/src/danog/MadelineProto/Loop/ResumableLoopInterface.php):  
```php
namespace danog\MadelineProto\Loop;

interface ResumableLoopInterface extends LoopInterface
{
    /**
     * Pause the loop.
     *
     * @param int $time For how long to pause the loop, if null will pause forever (until resume is called from outside of the loop)
     *
     * @return Promise
     */
    public function pause($time = null): Promise;

    /**
     * Resume the loop.
     *
     * @return void
     */
    public function resume();
}
```

Usually one would extend the [ResumableSignalLoop implementation](https://github.com/danog/MadelineProto/blob/master/src/danog/MadelineProto/Loop/Impl/ResumableSignalLoop.php).  
An example implementation can be seen in the [ResumableSignalLoop section of this page](#resumablesignalloop).  

#### SignalLoop

Yet another loop interface that exposes APIs to send signals to the loop, useful to force the termination of a loop from the outside, or to send data into it.  

[Interface](https://github.com/danog/MadelineProto/blob/master/src/danog/MadelineProto/Loop/SignalLoopInterface.php):  
```php
namespace danog\MadelineProto\Loop;

interface SignalLoopInterface extends LoopInterface
{
    /**
     * Resolve the promise or return|throw the signal.
     *
     * @param Promise $promise The origin promise
     *
     * @return Promise
     */
    public function waitSignal($promise): Promise;

    /**
     * Send a signal to the the loop.
     *
     * @param Exception|any $data Signal to send
     *
     * @return void
     */
    public function signal($data);
}

```

Usually one would extend the [ResumableSignalLoop implementation](https://github.com/danog/MadelineProto/blob/master/src/danog/MadelineProto/Loop/Impl/ResumableSignalLoop.php).  
An example implementation can be seen in the [ResumableSignalLoop section of this page](#resumablesignalloop).  
If you want, you can also extend only the [SignalLoop implementation](https://github.com/danog/MadelineProto/blob/master/src/danog/MadelineProto/Loop/Impl/SignalLoop.php), but usually a combination of the SignalLoop and ResumableLoop implementations is used, so read on to find out how to do that.  

#### ResumableSignalLoop

This is what you would usually use to build a full async loop.  
All loop interfaces and loop implementations are combined into one single abstract class you can extend.  

```php
use danog\MadelineProto\Loop\Impl\ResumableSignalLoop;
class MySuperLoop extends ResumableSignalLoop
{
    private $timeout;
    public function __construct($API, $timeout)
    {
        $this->API = $API;
        $this->timeout = $timeout;
    }
    public function loop()
    {
        $MadelineProto = $this->API;
        $logger = &$MadelineProto->logger;

        while (true) {
            $t = time();

            $result = yield $this->waitSignal($this->pause($this->timeout));
            if ($result <= 0) {
                return;
            } else if ($result > 0) {
                $this->timeout = $result;
            }
            
            $t = time() - $t;
            
            $result = yield $MadelineProto->messages->sendMessage(
                [
                    'peer'    => '...',
                    'message' => "Resumed after $t seconds of timeout"
                ]
            );
        }
    }
    public function __toString(): string
    {
        return "my cron signal loop";
    }
}
```

[ResumableSignalLoop implementation](https://github.com/danog/MadelineProto/blob/master/src/danog/MadelineProto/Loop/Impl/ResumableSignalLoop.php).  
As with the [Loop](#loop).  

The difference now is that you can use the `pause` method to pause execution of the loop for a certain period of time (in seconds, supports decimals).  
If `null` is passed, execution will be suspended forever (or until `resume` is called from outside of the loop).  

If the promise returned by `pause` (or by any other async method) is passed to `waitSignal`, and the result is yielded, execution will be suspended for the specified amount of time|forever, or until a signal is received through the `signal` method.  
The passed signal will then be returned as result of the `waitSignal` method, and can be used to stop the loop, or simply as a message exchange mechanism.  

#### GenericLoop

If you want a simpler way to use the `ResumableSignalLoop`, you can use the [GenericLoop](https://github.com/danog/MadelineProto/blob/master/src/danog/MadelineProto/Loop/Generic/GenericLoop.php).  
The constructor accepts three parameters:
```php
    /**
     * Constructor
     *
     * @param \danog\MadelineProto\API $API Instance of MadelineProto
     * @param callback $callback Callback to run
     * @param string $name Fetcher name
     */
    public function __construct($API, $callback, $name) { // ...
```

Example:
```php
use danog\MadelineProto\Loop\Generic\GenericLoop;
$loop = new GenericLoop(
    $MadelineProto,
    function () {
        yield $this->API->messages->sendMessage(['peer' => '...', 'message' => 'Hi every 2 seconds']);

        return 2;
    },
    "My super loop"
);
$loop->start();
```
The callback will be bound to the GenericLoop instance: this means that you will be able to use `$this` as if the callback were actually the `loop` function (you can access the API property, use the pause/waitSignal methods & so on).  
The return value of the callable can be:
* A number - the loop will be paused for the specified number of seconds
* `GenericLoop::STOP` - The loop will stop
* `GenericLoop::PAUSE` - The loop will pause forever (or until the `resume` method is called on the loop object from outside the loop)
* `GenericLoop::CONTINUE` - Return this if you want to rerun the loop without waiting

<a href="https://docs.madelineproto.xyz/docs/CREATING_A_CLIENT.html">Next section</a>
