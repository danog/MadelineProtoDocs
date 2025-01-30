---
title: "webPageAttributeStickerSet"
description: "Contains info about a stickerset », for a webPage preview of a stickerset deep link » (the webPage will have a type of telegram_stickerset)."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webPageAttributeStickerSet  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about a [stickerset »](https://core.telegram.org/api/stickers), for a [webPage](../constructors/webPage.html) preview of a [stickerset deep link »](https://core.telegram.org/api/links#stickerset-links) (the [webPage](../constructors/webPage.html) will have a `type` of `telegram_stickerset`).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|emojis|[Bool](/API_docs/types/Bool.html) | Optional|Whether this i s a [custom emoji stickerset](https://core.telegram.org/api/custom-emoji).|
|text\_color|[Bool](/API_docs/types/Bool.html) | Optional|Whether the color of this TGS custom emoji stickerset should be changed to the text color when used in messages, the accent color if used as emoji status, white on chat photos, or another appropriate color based on context.|
|stickers|Array of [Document](/API_docs/types/Document.html) | Yes|A subset of the stickerset in the stickerset.|



### Type: [WebPageAttribute](/API_docs/types/WebPageAttribute.html)


### Example:

```
$webPageAttributeStickerSet = ['_' => 'webPageAttributeStickerSet', 'emojis' => Bool, 'text_color' => Bool, 'stickers' => [Document, Document]];
```  
