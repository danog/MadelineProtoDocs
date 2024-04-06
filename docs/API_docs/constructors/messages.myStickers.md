---
title: "messages.myStickers"
description: "messages.myStickers attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_myStickers.html
---
# Constructor: messages.myStickers  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.html) | Yes|
|sets|Array of [StickerSetCovered](/API_docs/types/StickerSetCovered.html) | Yes|



### Type: [messages.MyStickers](/API_docs/types/messages.MyStickers.html)


### Example:

```
$messages_myStickers = ['_' => 'messages.myStickers', 'count' => int, 'sets' => [StickerSetCovered, StickerSetCovered]];
```  
