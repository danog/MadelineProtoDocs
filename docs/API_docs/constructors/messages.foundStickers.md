---
title: "messages.foundStickers"
description: "messages.foundStickers attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_foundStickers.html
---
# Constructor: messages.foundStickers  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|next\_offset|[int](/API_docs/types/int.html) | Optional|
|hash|[long](/API_docs/types/long.html) | Yes|
|stickers|Array of [Document](/API_docs/types/Document.html) | Yes|



### Type: [messages.FoundStickers](/API_docs/types/messages.FoundStickers.html)


### Example:

```
$messages_foundStickers = ['_' => 'messages.foundStickers', 'next_offset' => int, 'hash' => long, 'stickers' => [Document, Document]];
```  
