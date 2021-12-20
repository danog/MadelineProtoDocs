---
title: "messages.getOldFeaturedStickers"
description: "Method for fetching previously featured stickers"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getOldFeaturedStickers.html
---
# Method: messages.getOldFeaturedStickers
[Back to methods index](index.md)



Method for fetching previously featured stickers

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|offset|[int](../types/int.md) | Offset | Yes|
|limit|[int](../types/int.md) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Yes|
|hash|[long](../types/long.md) |  | Yes|


### Return type: [messages.FeaturedStickers](../types/messages.FeaturedStickers.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_FeaturedStickers = $MadelineProto->messages->getOldFeaturedStickers(['offset' => int, 'limit' => int, 'hash' => long, ]);
```

Or, if you're into Lua:

```lua
messages_FeaturedStickers = messages.getOldFeaturedStickers({offset=int, limit=int, hash=long, })
```

