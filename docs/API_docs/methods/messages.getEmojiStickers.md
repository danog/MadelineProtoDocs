---
title: "messages.getEmojiStickers"
description: "messages.getEmojiStickers parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getEmojiStickers.html
---
# Method: messages.getEmojiStickers
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[long](/API_docs/types/long.html) | Optional|


### Return type: [messages.AllStickers](/API_docs/types/messages.AllStickers.html)

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
$messages_AllStickers = $MadelineProto->messages->getEmojiStickers(hash: long, );
```

