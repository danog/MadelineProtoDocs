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
|hash|[string](../types/string.md) | Yes|Hash|
|sets|Array of [StickerSet](../types/StickerSet.md) | Yes|Sets|



### Type: [messages.AllStickers](../types/messages.AllStickers.md)


### Example:

```php
$messages.allStickers = ['_' => 'messages.allStickers', 'hash' => 'string', 'sets' => [StickerSet, StickerSet]];
```  


Or, if you're into Lua:

```lua
messages.allStickers={_='messages.allStickers', hash='string', sets={StickerSet}}

```


