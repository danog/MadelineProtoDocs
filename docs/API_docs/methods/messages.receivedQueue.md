---
title: "messages.receivedQueue"
description: "You cannot use this method directly"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_receivedQueue.html
---
# Method: messages.receivedQueue
[Back to methods index](index.html)



You cannot use this method directly

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|max\_qts|[int](/API_docs/types/int.html) | Maximum qts value available at the client | Yes|


### Return type: [Vector\_of\_long](/API_docs/types/long.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Vector_of_long = $MadelineProto->messages->receivedQueue(max_qts: int, );
```

