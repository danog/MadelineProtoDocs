---
title: "messages.readFeaturedStickers"
description: "Mark new featured stickers as read"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_readFeaturedStickers.html
---
# Method: messages.readFeaturedStickers
[Back to methods index](index.md)



Mark new featured stickers as read

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|Array of [long](../types/long.md) | IDs of stickersets to mark as read | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->readFeaturedStickers(['id' => [long, long], ]);
```

Or, if you're into Lua:

```lua
Bool = messages.readFeaturedStickers({id={long}, })
```

