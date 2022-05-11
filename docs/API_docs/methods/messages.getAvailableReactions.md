---
title: "messages.getAvailableReactions"
description: "Obtain available [message reactions »](https://core.telegram.org/api/reactions)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getAvailableReactions.html
---
# Method: messages.getAvailableReactions
[Back to methods index](index.html)



Obtain available [message reactions »](https://core.telegram.org/api/reactions)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [int](/API_docs/types/int.html) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Optional|


### Return type: [messages.AvailableReactions](/API_docs/types/messages.AvailableReactions.html)

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
$messages_AvailableReactions = $MadelineProto->messages->getAvailableReactions(hash: [int, int], );
```

