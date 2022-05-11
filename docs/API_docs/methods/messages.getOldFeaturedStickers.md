---
title: "messages.getOldFeaturedStickers"
description: "Method for fetching previously featured stickers"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getOldFeaturedStickers.html
---
# Method: messages.getOldFeaturedStickers
[Back to methods index](index.html)



Method for fetching previously featured stickers

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|offset|[int](/API_docs/types/int.html) | Offset | Yes|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Yes|
|hash|[long](/API_docs/types/long.html) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Yes|


### Return type: [messages.FeaturedStickers](/API_docs/types/messages.FeaturedStickers.html)

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
$messages_FeaturedStickers = $MadelineProto->messages->getOldFeaturedStickers(offset: int, limit: int, hash: long, );
```

