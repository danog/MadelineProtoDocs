---
title: "messages.allStickers"
description: "Info about all installed stickers"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_allStickers.html
---
# Constructor: messages.allStickers  
[Back to constructors index](/API_docs/constructors/index.html)



Info about all installed stickers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.html) | Yes|[Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|sets|Array of [StickerSet](/API_docs/types/StickerSet.html) | Yes|All stickersets|



### Type: [messages.AllStickers](/API_docs/types/messages.AllStickers.html)


### Example:

```
$messages_allStickers = ['_' => 'messages.allStickers', 'hash' => long, 'sets' => [StickerSet, StickerSet]];
```  
