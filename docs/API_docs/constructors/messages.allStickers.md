---
title: "messages.allStickers"
description: "Info about all installed stickers"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_allStickers.html
---
# Constructor: messages.allStickers  
[Back to constructors index](index.md)



Info about all installed stickers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](../types/long.md) | Yes|
|sets|Array of [StickerSet](../types/StickerSet.md) | Yes|All stickersets|



### Type: [messages.AllStickers](../types/messages.AllStickers.md)


### Example:

```php
$messages_allStickers = ['_' => 'messages.allStickers', 'hash' => long, 'sets' => [StickerSet, StickerSet]];
```  


Or, if you're into Lua:

```lua
messages_allStickers={_='messages.allStickers', hash=long, sets={StickerSet}}

```


