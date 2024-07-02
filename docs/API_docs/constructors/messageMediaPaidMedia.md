---
title: "messageMediaPaidMedia"
description: "messageMediaPaidMedia attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaPaidMedia  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|stars\_amount|[long](/API_docs/types/long.html) | Yes|
|extended\_media|Array of [MessageExtendedMedia](/API_docs/types/MessageExtendedMedia.html) | Yes|



### Type: [MessageMedia](/API_docs/types/MessageMedia.html)


### Example:

```
$messageMediaPaidMedia = ['_' => 'messageMediaPaidMedia', 'stars_amount' => long, 'extended_media' => [MessageExtendedMedia, MessageExtendedMedia]];
```  
