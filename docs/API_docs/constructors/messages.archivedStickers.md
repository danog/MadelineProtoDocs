---
title: "messages.archivedStickers"
description: "Archived stickersets"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_archivedStickers.html
---
# Constructor: messages.archivedStickers  
[Back to constructors index](/API_docs/constructors/index.html)



Archived stickersets

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Number of archived stickers|
|sets|Array of [StickerSetCovered](/API_docs/types/StickerSetCovered.html) | Yes|Archived stickersets|



### Type: [messages.ArchivedStickers](/API_docs/types/messages.ArchivedStickers.html)


### Example:

```
$messages_archivedStickers = ['_' => 'messages.archivedStickers', 'count' => int, 'sets' => [StickerSetCovered, StickerSetCovered]];
```  
