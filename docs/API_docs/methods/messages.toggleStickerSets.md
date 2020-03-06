---
title: messages.toggleStickerSets
description: messages.toggleStickerSets parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_toggleStickerSets.html
---
# Method: messages.toggleStickerSets  
[Back to methods index](index.md)


### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|uninstall|[Bool](../types/Bool.md) | Optional|
|archive|[Bool](../types/Bool.md) | Optional|
|unarchive|[Bool](../types/Bool.md) | Optional|
|stickersets|Array of [InputStickerSet](../types/InputStickerSet.md) | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->toggleStickerSets(['uninstall' => Bool, 'archive' => Bool, 'unarchive' => Bool, 'stickersets' => [InputStickerSet, InputStickerSet], ]);
```

Or, if you're into Lua:

```lua
Bool = messages.toggleStickerSets({uninstall=Bool, archive=Bool, unarchive=Bool, stickersets={InputStickerSet}, })
```

