---
title: "messages.featuredStickers"
description: "Featured stickersets"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_featuredStickers.html
---
# Constructor: messages.featuredStickers  
[Back to constructors index](/API_docs/constructors/index.html)



Featured stickersets

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.html) | Yes|[Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|count|[int](/API_docs/types/int.html) | Yes|Total number of featured stickers|
|sets|Array of [StickerSetCovered](/API_docs/types/StickerSetCovered.html) | Yes|Featured stickersets|
|unread|Array of [long](/API_docs/types/long.html) | Yes|IDs of new featured stickersets|



### Type: [messages.FeaturedStickers](/API_docs/types/messages.FeaturedStickers.html)


### Example:

```
$messages_featuredStickers = ['_' => 'messages.featuredStickers', 'hash' => long, 'count' => int, 'sets' => [StickerSetCovered, StickerSetCovered], 'unread' => [long, long]];
```  
