---
title: "messages.myStickers"
description: "The list of stickersets owned by the current account »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_myStickers.html
---
# Constructor: messages.myStickers  
[Back to constructors index](/API_docs/constructors/index.html)



The list of [stickersets owned by the current account »](https://core.telegram.org/api/stickers).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Total number of owned stickersets.|
|sets|Array of [StickerSetCovered](/API_docs/types/StickerSetCovered.html) | Yes|Stickersets|



### Type: [messages.MyStickers](/API_docs/types/messages.MyStickers.html)


### Example:

```
$messages_myStickers = ['_' => 'messages.myStickers', 'count' => int, 'sets' => [StickerSetCovered, StickerSetCovered]];
```  
