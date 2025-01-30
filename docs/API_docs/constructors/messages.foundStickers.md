---
title: "messages.foundStickers"
description: "Found stickers"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_foundStickers.html
---
# Constructor: messages.foundStickers  
[Back to constructors index](/API_docs/constructors/index.html)



Found stickers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|next\_offset|[int](/API_docs/types/int.html) | Optional|Offset for [pagination](https://core.telegram.org/api/offsets)|
|hash|[long](/API_docs/types/long.html) | Yes|[Hash used for caching, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|stickers|Array of [Document](/API_docs/types/Document.html) | Yes|Found stickers|



### Type: [messages.FoundStickers](/API_docs/types/messages.FoundStickers.html)


### Example:

```
$messages_foundStickers = ['_' => 'messages.foundStickers', 'next_offset' => int, 'hash' => long, 'stickers' => [Document, Document]];
```  
