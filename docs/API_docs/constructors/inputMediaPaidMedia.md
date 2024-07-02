---
title: "inputMediaPaidMedia"
description: "inputMediaPaidMedia attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaPaidMedia  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|stars\_amount|[long](/API_docs/types/long.html) | Yes|
|extended\_media|Array of [MessageMedia, Message, Update or InputMedia](/API_docs/types/InputMedia.html) | Yes|



### Type: [InputMedia](/API_docs/types/InputMedia.html)


### Example:

```
$inputMediaPaidMedia = ['_' => 'inputMediaPaidMedia', 'stars_amount' => long, 'extended_media' => [InputMedia, InputMedia]];
```  
