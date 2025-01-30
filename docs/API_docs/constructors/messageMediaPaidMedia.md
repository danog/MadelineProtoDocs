---
title: "messageMediaPaidMedia"
description: "Paid media, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaPaidMedia  
[Back to constructors index](/API_docs/constructors/index.html)



[Paid media, see here »](https://core.telegram.org/api/paid-media) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|stars\_amount|[long](/API_docs/types/long.html) | Yes|The price of the media in [Telegram Stars](https://core.telegram.org/api/stars).|
|extended\_media|Array of [MessageExtendedMedia](/API_docs/types/MessageExtendedMedia.html) | Yes|Either the paid-for media, or super low resolution media previews if the media wasn't purchased yet, [see here »](https://core.telegram.org/api/paid-media#viewing-paid-media) for more info.|



### Type: [MessageMedia](/API_docs/types/MessageMedia.html)


### Example:

```
$messageMediaPaidMedia = ['_' => 'messageMediaPaidMedia', 'stars_amount' => long, 'extended_media' => [MessageExtendedMedia, MessageExtendedMedia]];
```  
