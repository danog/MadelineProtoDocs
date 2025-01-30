---
title: "messageExtendedMediaPreview"
description: "Paid media preview for not yet purchased paid media, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageExtendedMediaPreview  
[Back to constructors index](/API_docs/constructors/index.html)



Paid media preview for not yet purchased paid media, [see here »](https://core.telegram.org/api/paid-media) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|w|[int](/API_docs/types/int.html) | Optional|Width|
|h|[int](/API_docs/types/int.html) | Optional|Height|
|thumb|[PhotoSize](/API_docs/types/PhotoSize.html) | Optional|[Extremely low resolution thumbnail](https://core.telegram.org/api/files#stripped-thumbnails).|
|video\_duration|[int](/API_docs/types/int.html) | Optional|Video duration for videos.|



### Type: [MessageExtendedMedia](/API_docs/types/MessageExtendedMedia.html)


### Example:

```
$messageExtendedMediaPreview = ['_' => 'messageExtendedMediaPreview', 'w' => int, 'h' => int, 'thumb' => PhotoSize, 'video_duration' => int];
```  
