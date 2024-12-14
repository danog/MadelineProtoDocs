---
title: "messages.getFeaturedEmojiStickers"
description: "Gets featured custom emoji stickersets."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getFeaturedEmojiStickers.html
---
# Method: messages.getFeaturedEmojiStickers
[Back to methods index](index.html)



Gets featured custom emoji stickersets.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Optional|


### Return type: [messages.FeaturedStickers](/API_docs/types/messages.FeaturedStickers.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_FeaturedStickers = $MadelineProto->messages->getFeaturedEmojiStickers(hash: [$long\|string, $long\|string], );
```

