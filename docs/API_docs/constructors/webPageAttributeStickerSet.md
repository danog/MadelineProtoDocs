---
title: "webPageAttributeStickerSet"
description: "webPageAttributeStickerSet attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webPageAttributeStickerSet  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|emojis|[Bool](/API_docs/types/Bool.html) | Optional|
|text\_color|[Bool](/API_docs/types/Bool.html) | Optional|
|stickers|Array of [Document](/API_docs/types/Document.html) | Yes|



### Type: [WebPageAttribute](/API_docs/types/WebPageAttribute.html)


### Example:

```
$webPageAttributeStickerSet = ['_' => 'webPageAttributeStickerSet', 'emojis' => Bool, 'text_color' => Bool, 'stickers' => [Document, Document]];
```  
