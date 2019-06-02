---
title: http_wait
description: Makes the server send messages waiting in the buffer
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: http\_wait  
[Back to methods index](index.md)


Makes the server send messages waiting in the buffer

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|max\_delay|[int](../types/int.md) | Denotes the maximum number of milliseconds that has elapsed between the first message for this session and the transmission of an HTTP response | Yes|
|wait\_after|[int](../types/int.md) | After the receipt of the latest message for a particular session, the server waits another wait_after milliseconds in case there are more messages. If there are no additional messages, the result is transmitted (a container with all the messages). | Yes|
|max\_wait|[int](../types/int.md) | If more messages appear, the wait_after timer is reset. | Yes|


### Return type: [HttpWait](../types/HttpWait.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$HttpWait = $MadelineProto->http_wait(['max_delay' => int, 'wait_after' => int, 'max_wait' => int, ]);
```

Or, if you're into Lua:

```lua
HttpWait = http_wait({max_delay=int, wait_after=int, max_wait=int, })
```

