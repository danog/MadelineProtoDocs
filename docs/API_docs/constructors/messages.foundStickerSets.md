---
title: "messages.foundStickerSets"
description: "Found stickersets"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_foundStickerSets.html
---
# Constructor: messages.foundStickerSets  
[Back to constructors index](/API_docs/constructors/index.html)



Found stickersets

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.html) | Yes|[Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|sets|Array of [StickerSetCovered](/API_docs/types/StickerSetCovered.html) | Yes|Found stickersets|



### Type: [messages.FoundStickerSets](/API_docs/types/messages.FoundStickerSets.html)


### Example:

```
$messages_foundStickerSets = ['_' => 'messages.foundStickerSets', 'hash' => long, 'sets' => [StickerSetCovered, StickerSetCovered]];
```  
