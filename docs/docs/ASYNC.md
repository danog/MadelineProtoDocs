---
title: "Async"
description: "MadelineProto now features async, for incredible speed improvements, and parallel processing.  "
nav_order: 23
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Async

MadelineProto now features async, for **incredible speed improvements**, and parallel processing.  
Powered by [amphp](https://amphp.org), MadelineProto wraps the AMPHP APIs to provide a simpler generator-based async API.  

* [Usage](#usage)
  * [Enabling the MadelineProto async API](#enabling-the-madelineproto-async-api)
  * [Using the MadelineProto async API](#using-the-madelineproto-async-api)
    * [Async in event handler](#async-in-event-handler)
    * [Async in callback handler](#async-in-callback-handler)
    * [Wrapped async](#wrapped-async)
    * [Multiple async](#multiple-async)
    * [ArrayAccess async](#arrayaccess-async)
    * [Ignored async](#ignored-async)
    * [Blocking async](#blocking-async)
  * [MadelineProto and AMPHP async APIs](#madelineproto-and-amphp-async-apis)
    * [Helper methods](#helper-methods)
      * [Async sleep](#async-sleep-does-not-block-the-main-thread)
      * [Async readline](#async-readline-does-not-block-the-main-thread)
      * [Async echo](#async-echo-does-not-block-the-main-thread)
      * [MadelineProto HTTP client](#madelineproto-http-client)
      * [Async forking](#async-forking-does-green-thread-forking)
      * [Async flock](#async-flock)
      * [Combining async operations](#combining-async-operations)
    * [MadelineProto async loop APIs](#async-loop-apis)
      * [Loop](#loop)
      * [ResumableLoop](#resumableloop)
      * [SignalLoop](#signalloop)
      * [ResumableSignalLoop](#resumablesignalloop)
      * [GenericLoop](#genericloop)
      * [PeriodicLoop](#periodicloop)

## Usage

What exactly __is__ **async**, you may ask, and how is it better than **threading** or **multiprocessing**?  
Async is a relatively new programming pattern that allows you to easily write **non-blocking** code **as if you were using standard** blocking functions, all **without** the need for complex message exchange systems and synchronization handling for threaded programs, that only add overhead and complexity to your programs, making everything slower and error-prone.  

That's very cool and all, you might think, but how exactly does this __async__ stuff work? Well, as it turns out, it's very easy.  

Instead of writing code like this:  
```php
$file = $MadelineProto->downloadToDir($bigfile, '/tmp/');
```

Write it like **this**:  
```php
$file = yield $MadelineProto->downloadToDir($bigfile, '/tmp/');
```

### That's it.

It's really **that** easy, you just have to add a `yield` before calling MadelineProto methods.  
The `yield` will automatically **suspend** the execution of the function, letting the program do other stuff while the file is being downloaded.  
Once the file is downloaded, execution is automatically **resumed** from that exact point in the function.  

This means that you can handle multiple updates, download/upload multiple files all together in one process, as if you were writing normal synchronous code + making everything a lot faster.  

If your code still relies on the old synchronous behaviour, don't worry, there is backward compatibility.  
However, I highly recommend you switch to async, due to the huge performance and parallelism benefits.  

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
    $id = (yield $MadelineProto->getInfo($chatID, ['async' => true]))['bot_api_id'];
    $res = yield $MadelineProto->messages->sendMesssage(['peer' => $chatID, 'message' => "Message from: $id\n$message"], ['async' => true]);
    return $res;
};
$result = $sm('@danogentili', 'hi');
```

This **will not work**, because the result of a function that uses `yield` is not the `return`ed value, but a [generator](https://www.php.net/manual/en/language.generators.overview.php), which is what the async AMPHP API is based on.  
If the generator is not __passed to the AMPHP event loop__, execution of the function will not be resumed: when MadelineProto asynchronously obtains the result of the getInfo, execution of the function is never resumed, and the line with sendMessage is never called.  
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
            yield $this->downloadToDir($update, '/tmp');
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
        yield $this->messages->sendMessage(peer: $peer, message: $message, reply_to_msg_id: isset($update['message']['id']) ? $update['message']['id'] : null, parse_mode: 'HTML');
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
    yield $MadelineProto->messages->sendMessage(peer: $update, message: 'Hi after 3 seconds');
});
```

### Wrapped async
```php
$MadelineProto->async(true);
$MadelineProto->loop(function () use ($MadelineProto) {
    yield $MadelineProto->messages->sendMessage(peer: '...', message: 'hi');
    // You can also have an asynchronous get_updates (deprecated) loop in here, if you want to; just don't forget to use yield for all MadelineProto functions.
});
```

You can pass a promise or an async function to the loop function, and it will block until it is resolved.  

### Ignored async
```php
$MadelineProto->messages->sendMessage(['peer' => '@danogentili', 'message' => 'a'], ['async' => true]);
$MadelineProto->messages->sendMessage(['peer' => '@danogentili', 'message' => 'b'], ['async' => true]);
```

You can use the async version of MadelineProto functions **without** yield if you don't want the request to block, and you don't need the result of the function.  
This is allowed, but the order of the function calls will not be guaranteed: you can use [call queues](https://docs.madelineproto.xyz/docs/USING_METHODS.html#queues) if you want to make sure the order of the calls remains the same.
See [async forking](#async-forking-does-async-green-thread-forking).  

### Multiple async
```php
yield $MadelineProto->messages->sendMessage([
    'multiple' => true,
    ['peer' => '@danogentili', 'message' => 'hi'],
    ['peer' => '@apony', 'message' => 'hi']
]);
```

This is the preferred way of combining multiple method calls: this way, the MadelineProto async WriteLoop will combine all method calls in one container, making everything WAY faster.  
The result of this will be an array of results, whose type is determined by the original return type of the method (see [API docs](https://docs.madelineproto.xyz/API_docs)).  

The order of method calls can be guaranteed (server-side, not by MadelineProto) by using [call queues](USING_METHODS.html#queues).

### ArrayAccess async

You can do async ArrayAccess on promises.  

Now instead of doing this:  
```php
$id = (yield $MadelineProto->getPwrChat('danogentili'))['bot_api_id'];
```

You can simply do this:  
```php
$id = yield $MadelineProto->getPwrChat('danogentili')['bot_api_id'];
```

Setting attributes asynchronously is also supported (it's kind of useless, but it's useful if you have some custom logic, like for example a method that returns a custom ArrayAccess class with a set method that does something magical).  
```php
$Id = yield $MadelineProto->getPwrChat('danogentili')['bot_api_id'] = 'pony';
```

isset and unset aren't supported due to the fact that in PHP, isset and unset aren't proper functions but language constructs (logically).  
You have to do this, instead:  
```php
$set = isset((yield $MadelineProto->getPwrChat('danogentili'))['bot_api_id']);
```

or  
```php
$result = yield $MadelineProto->getPwrChat('danogentili');
$set = isset($result['bot_api_id']);
```

Also, `ArrayAccess` on raw generators still isn't supported unless you wrap them in a coroutine using `$MadelineProto->call`:  
```php
public function ponyAsync()
{
    return yield $MadelineProto->getInfo('danogentili');
}
// public function onUpdateNewMessage....

// WILL NOT WORK
$set = yield $this->ponyAsync()['id'];

// Will work
$set = (yield $this->ponyAsync())['id'];

// Will work
$set = $MadelineProto->call(yield $this->ponyAsync())['id'];

public function pony()
{
    return $MadelineProto->call($this->ponyAsync());
}

// Will work
$set = yield $this->pony()['id'];
```


### Blocking async
```php
$result = blocking_function();
```

Sometimes, you have to call non-async functions in your code: that is allowed in async MadelineProto, you just have to call your functions normally without `yield`.  
However, you shouldn't do (or need to do) this, because this renders async completely useless.  
AMPHP and MadelineProto already provide async versions of curl, `file_get_contents`, MySQL, redis, postgres, and many more native PHP functions: 

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

#### Async readline (does not block the main thread)
```php
$res = yield $MadelineProto->readLine('Optional prompt');
```

#### Async echo (does not block the main thread)
```php
yield $MadelineProto->echo('Hello'.PHP_EOL);
```

#### MadelineProto HTTP client

When using amphp's [http-client](https://amphp.org/http-client) to make high-speed asynchronous HTTP requests (downloading files, etc.), use MadelineProto's modified http-client client, instead.  
It automatically supports the socks/HTTP proxies specified in MadelineProto's settings (will use proxies only if the file can't be downloaded normally), and soon DoH for greater security.  

To use MadelineProto's http-client client, instead of creating an http-client instance:  
```php
$client = \Amp\Http\Client\HttpClientBuilder::buildDefault();
```

Simply get MadelineProto's HTTP client:  
```php
$client = $MadelineProto->getHTTPClient();
```

From here it's like in the [http-client docs](https://amphp.org/http-client).  

MadelineProto also provides a simplified async version of `file_get_contents`:  
```php
$result = yield $MadelineProto->fileGetContents('https://myurl');
```

#### Async forking (does async green-thread forking)

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

#### Async flock

```php
$unlock = yield $MadelineProto->flock($filePath, LOCK_SH);
try {
    // ...
} finally {
    $unlock();
}
```

This will asynchronously wait for a lock on `$filePath` (creating it if it doesn't exist).  
The locking mode can be `LOCK_SH` (shared locks), `LOCK_EX` (exclusive locks), as with the PHP `flock` function.  
A third optional parameter can be set, to specify a polling interval in seconds (0.1 by default).  

#### Combining async operations

These methods can be used to execute multiple async operations simultaneously and wait for the result of all of them.  
Each method has different error handling techniques, see the [amphp docs](https://amphp.org/amp/promises/combinators).  
Note that if you just take the result of these methods without yielding it, you can use it as a normal promise/generator.  

**Note**: this is not the recommended method to make multiple method calls on the same instance of MadelineProto; use this only for non-API methods like `start()`; for API methods, use [multiple async](#multiple-async).  

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
namespace danog\Loop;

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
The `start` method returns a promise that resolves when the loop finishes running.  
Multiple calls to `start` will be ignored, logging an error and returning `false` instead of `true`.  
You can use the `isRunning` method to check if the loop is already running.  
The `__toString` method still has to be implemented in order to get the name of the loop, that will be used by the MadelineProto logging mechanism every time the loop starts/exits/fails to start.  
By default, an instance of MadelineProto MUST be passed to the constructor of the function, or **if** a custom constructor is defined, the `$this->API` property MUST be set to an instance of MadelineProto.  

```php
use danog\Loop;
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

The loop can be instantiated and `start()`ed, and this will automatically run the code in the loop in background.  
If, however, only your loop is started (without an event handling loop), you have to pass the promise returned by `$loop->start()` to `$MadelineProto->loop`.  
Do NOT do this if you've already started `$MadelineProto->loop()`.  
```php
$loop = new MyLoop;
$MadelineProto->loop($loop->start());
```

#### ResumableLoop

A way more useful loop that exposes APIs to pause and resume the execution of the loop, both from outside of the loop, and in a cron-like manner from inside of the loop.  

[Interface](https://github.com/danog/MadelineProto/blob/master/src/danog/MadelineProto/Loop/ResumableLoopInterface.php):  
```php
namespace danog\Loop;

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
namespace danog\Loop;

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
use danog\Loop\ResumableSignalLoop;
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
                peer:    '...',
                message: "Resumed after $t seconds of timeout"
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
use danog\Loop\Generic\GenericLoop;
$loop = new GenericLoop(
    $MadelineProto,
    function () {
        yield $this->API->messages->sendMessage(peer: '...', message: 'Hi every 2 seconds');

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

If the callable does not return anything, the loop will behave is if `GenericLoop::PAUSE` was returned.  

#### PeriodicLoop

If you simply want to execute an action every N seconds, [PeriodicLoop](https://github.com/danog/MadelineProto/blob/master/src/danog/MadelineProto/Loop/Generic/PeriodicLoop.php) is the way to go.  
The constructor accepts four parameters:
```php
    /**
     * Constructor.
     *
     * @param \danog\MadelineProto\API $API      Instance of MTProto class
     * @param callable                 $callback Callback to call
     * @param string                   $name     Loop name
     * @param int|float                $timeout  Loop timeout
     */
    public function __construct($API, callable $callback, string $name, $timeout) { // ...
```

Example:
```php
use danog\Loop\Generic\PeriodicLoop;
$loop = new PeriodicLoop(
    $MadelineProto,
    function () use (&$loop) {
        yield $this->API->messages->sendMessage(peer: '...', message: 'Hi every 2 seconds');
    },
    "My super loop",
    2
);
$loop->start();
```
Unlike `GenericLoop`, the callback will **not** be bound to the GenericLoop instance.
You can still command the loop by using the pause/waitSignal methods from the outside or by capturing the loop instance in a closure like shown above.  

<a href="https://docs.madelineproto.xyz/docs/USING_METHODS.html">Next section</a>