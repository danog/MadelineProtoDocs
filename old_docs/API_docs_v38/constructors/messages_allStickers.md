---
title: messages.allStickers
description: All stickers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.allStickers  
[Back to constructors index](index.md)



All stickers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[string](../types/string.md) | Yes|Hash|
|sets|Array of [StickerSet](../types/StickerSet.md) | Yes|Sets|



### Type: [messages\_AllStickers](../types/messages_AllStickers.md)


### Example:

```php
$messages_allStickers = ['_' => 'messages.allStickers', 'hash' => 'string', 'sets' => [StickerSet, StickerSet]];
```  


Or, if you're into Lua:

```lua
messages_allStickers={_='messages.allStickers', hash='string', sets={StickerSet}}

```


