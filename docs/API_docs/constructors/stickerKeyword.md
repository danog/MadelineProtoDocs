---
title: "stickerKeyword"
description: "Keywords for a certain sticker"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: stickerKeyword  
[Back to constructors index](/API_docs/constructors/index.html)



Keywords for a certain sticker

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|document\_id|[long](/API_docs/types/long.html) | Yes|Sticker ID|
|keyword|Array of [string](/API_docs/types/string.html) | Yes|Keywords|



### Type: [StickerKeyword](/API_docs/types/StickerKeyword.html)


### Example:

```
$stickerKeyword = ['_' => 'stickerKeyword', 'document_id' => long, 'keyword' => ['string', 'string']];
```  
