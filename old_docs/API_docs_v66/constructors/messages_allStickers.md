---
title: messages.allStickers
description: Info about all installed stickers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.allStickers  
[Back to constructors index](index.md)



Info about all installed stickers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](../types/int.md) | Yes|[Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|sets|Array of [StickerSet](../types/StickerSet.md) | Yes|Sets|



### Type: [messages\_AllStickers](../types/messages_AllStickers.md)


### Example:

```php
$messages_allStickers = ['_' => 'messages.allStickers', 'hash' => int, 'sets' => [StickerSet, StickerSet]];
```  


Or, if you're into Lua:

```lua
messages_allStickers={_='messages.allStickers', hash=int, sets={StickerSet}}

```


