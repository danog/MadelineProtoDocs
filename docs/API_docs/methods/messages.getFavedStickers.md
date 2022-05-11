---
title: "messages.getFavedStickers"
description: "Get faved stickers"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getFavedStickers.html
---
# Method: messages.getFavedStickers
[Back to methods index](index.html)



Get faved stickers

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|[long](/API_docs/types/long.html) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Yes|


### Return type: [messages.FavedStickers](/API_docs/types/messages.FavedStickers.html)

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
$messages_FavedStickers = $MadelineProto->messages->getFavedStickers(hash: long, );
```

