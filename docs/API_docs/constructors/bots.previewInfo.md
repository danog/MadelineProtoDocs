---
title: "bots.previewInfo"
description: "bots.previewInfo attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/bots_previewInfo.html
---
# Constructor: bots.previewInfo  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|media|Array of [BotPreviewMedia](/API_docs/types/BotPreviewMedia.html) | Yes|
|lang\_codes|Array of [string](/API_docs/types/string.html) | Yes|



### Type: [bots.PreviewInfo](/API_docs/types/bots.PreviewInfo.html)


### Example:

```
$bots_previewInfo = ['_' => 'bots.previewInfo', 'media' => [BotPreviewMedia, BotPreviewMedia], 'lang_codes' => ['string', 'string']];
```  
