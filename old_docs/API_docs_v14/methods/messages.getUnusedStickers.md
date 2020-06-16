---
title: messages.getUnusedStickers
description: messages.getUnusedStickers parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getUnusedStickers.html
---
# Method: messages.getUnusedStickers
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|limit|[int](../types/int.md) | Yes|


### Return type: [Vector\_of\_StickerSetCovered](../types/StickerSetCovered.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_StickerSetCovered = $MadelineProto->messages->getUnusedStickers(['limit' => int, ]);
```

Or, if you're into Lua:

```lua
Vector_of_StickerSetCovered = messages.getUnusedStickers({limit=int, })
```

