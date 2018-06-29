---
title: messages.recentStickers
description: messages_recentStickers attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.recentStickers  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[int](../types/int.md) | Yes|
|packs|Array of [StickerPack](../types/StickerPack.md) | Yes|
|stickers|Array of [Document](../types/Document.md) | Yes|
|dates|Array of [int](../types/int.md) | Yes|



### Type: [messages\_RecentStickers](../types/messages_RecentStickers.md)


### Example:

```
$messages_recentStickers = ['_' => 'messages.recentStickers', 'hash' => int, 'packs' => [StickerPack, StickerPack], 'stickers' => [Document, Document], 'dates' => [int, int]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messages.recentStickers", "hash": int, "packs": [StickerPack], "stickers": [Document], "dates": [int]}
```


Or, if you're into Lua:  


```
messages_recentStickers={_='messages.recentStickers', hash=int, packs={StickerPack}, stickers={Document}, dates={int}}

```


