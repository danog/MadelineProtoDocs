---
title: "messages.featuredStickers"
description: "Featured stickersets"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_featuredStickers.html
---
# Constructor: messages.featuredStickers  
[Back to constructors index](/API_docs/constructors/index.md)



Featured stickersets

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.md) | Yes|
|count|[int](/API_docs/types/int.md) | Yes|Total number of featured stickers|
|sets|Array of [StickerSetCovered](/API_docs/types/StickerSetCovered.md) | Yes|Featured stickersets|
|unread|Array of [long](/API_docs/types/long.md) | Yes|IDs of new featured stickersets|



### Type: [messages.FeaturedStickers](/API_docs/types/messages.FeaturedStickers.md)


### Example:

```php
$messages_featuredStickers = ['_' => 'messages.featuredStickers', 'hash' => long, 'count' => int, 'sets' => [StickerSetCovered, StickerSetCovered], 'unread' => [long, long]];
```  
