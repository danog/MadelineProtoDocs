---
title: "messages.receivedQueue"
description: "You cannot use this method directly"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_receivedQueue.html
---
# Method: messages.receivedQueue
[Back to methods index](index.md)



You cannot use this method directly

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|max\_qts|[int](../types/int.md) | Maximum qts value available at the client | Yes|


### Return type: [Vector\_of\_long](../types/long.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_long = $MadelineProto->messages->receivedQueue(['max_qts' => int, ]);
```

Or, if you're into Lua:

```lua
Vector_of_long = messages.receivedQueue({max_qts=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|MAX_QTS_INVALID|The specified max_qts is invalid|
|400|MSG_WAIT_FAILED|A waiting call returned an error|


