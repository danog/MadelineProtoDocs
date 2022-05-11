---
title: "messages.getStickers"
description: "Get stickers by emoji"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getStickers.html
---
# Method: messages.getStickers
[Back to methods index](index.html)



Get stickers by emoji

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|emoticon|[string](/API_docs/types/string.html) | The emoji | Yes|
|hash|[long](/API_docs/types/long.html) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Yes|


### Return type: [messages.Stickers](/API_docs/types/messages.Stickers.html)

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
$messages_Stickers = $MadelineProto->messages->getStickers(emoticon: 'string', hash: long, );
```

