---
title: messages.getFeaturedStickers
description: Get featured stickers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getFeaturedStickers  
[Back to methods index](index.md)


Get featured stickers

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [int](../types/int.md) |  the hash parameter of the previous result of this method | Optional|


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

$messages.FeaturedStickers = $MadelineProto->messages->getFeaturedStickers(['hash' => [int, int], ]);
```

Or, if you're into Lua:

```lua
messages.FeaturedStickers = messages.getFeaturedStickers({hash={int}, })
```

