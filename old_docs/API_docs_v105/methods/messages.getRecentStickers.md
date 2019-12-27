---
title: messages.getRecentStickers
description: Get recent stickers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getRecentStickers  
[Back to methods index](index.md)


Get recent stickers

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|attached|[Bool](../types/Bool.md) | Get stickers recently attached to photo or video files | Optional|
|hash|Array of [int](../types/int.md) | IDs the hash parameter of the previous result of this method | Optional|


### Return type: [messages.RecentStickers](../types/messages.RecentStickers.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.RecentStickers = $MadelineProto->messages->getRecentStickers(['attached' => Bool, 'hash' => [int, int], ]);
```

Or, if you're into Lua:

```lua
messages.RecentStickers = messages.getRecentStickers({attached=Bool, hash={int}, })
```

