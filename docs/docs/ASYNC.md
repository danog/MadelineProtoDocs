---
title: Async
description: MadelineProto now features async, for **incredible speed improvements**, and parallel processing **without** buggy and slow threading/multiprocessing.  
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Async

MadelineProto now features async, for **incredible speed improvements**, and parallel processing **without** buggy and slow threading/multiprocessing.  
Powered by [amphp](https://amphp.org), MadelineProto wraps the AMPHP APIs to provide a simpler generator-based async API.  

* [Usage](#usage)
 * [Loading the latest version of MadelineProto](#loading-the-latest-version-of-madelineproto)
 * [Enabling the MadelineProto async API](#enabling-the-madelineproto-async-api)
 * [Using the MadelineProto async API](#using-the-madelineproto-async-api)
  * [Async in event handler](#async-in-event-handler)
  * [Async in callback handler](#async-in-callback-handler)
  * [Wrapped async](#wrapped-async)
  * [Ignored async](#ignored-async)
  * [MadelineProto and AMPHP async APIs](#madelineproto-and-amphp-async-apis)

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

## Enabling the MadelineProto async API

The `yield` operator can only be used within functions, once MadelineProto's async mode is enabled.  
To do that, simply run the `async` function, or pass the async enabler flag separately to each method call, if you want to make only some calls async.  

This will enable async mode for **all** MadelineProto functions:  
```php
$MadelineProto->async(true);
// ...
yield $MadelineProto->messages->sendMessage(...);
```

This will enable async mode for **only** for one specific call of a MadelineProto function (by adding a **new** array parameter after all the required parameters):  
```php
yield $MadelineProto->messages->sendMessage(..., ['async' => true]);
```

## Using the MadelineProto async API

As mentioned earlier, you can only use the `yield` operator within functions, but not just any function, for example:
```php
$sm = function ($chatID, $message) use ($MadelineProto) {
    $id = (yield $MadelineProto->get_info($chatID))['bot_api_id'];
    $res = yield $MadelineProto->messages->sendMesssage(['peer' => $chatID, 'message' => "Message from: $id\n$message"], ['async' => true]);
    return $res;
};
$result = $sm('@danogentili', 'hi');
```

This will **not** work, because the result of a function that uses `yield` is not the `return`ed value, but a [generator](https://www.php.net/manual/en/language.generators.overview.php), which is what the async AMPHP API is based on.  
If the generator is not __passed to the AMPHP event loop__, execution of the function will not be resumed: when MadelineProto asynchronously obtains the result of the get_info, execution of the function is never resumed, and the line with sendMessage is never called.  
To avoid this problem, only call asynchronous functions in the event/callback update handler, or in functions called by the event/callback update handler, or inside a function passed to loop.

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

## Ignored async
```php
$MadelineProto->messages->sendMessage(['peer' => '@danogentili', 'message' => 'a'], ['async' => true]);
$MadelineProto->messages->sendMessage(['peer' => '@danogentili', 'message' => 'b'], ['async' => true]);
```

You can use the async version of MadelineProto functions **without** yield if you don't want the request to block, and you don't need the result of the function.  
This is allowed, but the order of the function calls will not be guaranteed: you can use [call queues](https://docs.madelineproto.xyz/docs/USING_METHODS.html#queues) if you want to make sure the order of the calls remains the same.


## MadelineProto and AMPHP async APIs

MadelineProto and AMPHP both provide a lot of async functions: all of MadelineProto's functions are async, for example; and AMPHP provides [multiple packages](https://amphp.org/packages) to work asynchronously with HTTP requests, websockets, databases (MySQL, redis, postgres, DNS, sockets and [much more](https://github.com/amphp/)!  
When using AMPHP libraries, you just have to use them with yield, no need to start the event loop, as long as you're running the functions inside MadelineProto's update handler/loop.  

Also, you should read the AMPHP docs, especially the [event loop docs](https://amphp.org/amp/event-loop/api): AMPHP provides multiple helper methods for executing actions repeatedly every N seconds in a non-blocking manner, or to defer execution of certain actions (aka async cron).  

MadelineProto also provides a few generic async helper methods:  
```php
$MadelineProto->sleep(3); // Async sleep
```

<a href="https://docs.madelineproto.xyz/docs/CREATING_A_CLIENT.html">Next section</a>