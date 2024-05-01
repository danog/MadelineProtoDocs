---
title: "messageExtendedMediaPreview"
description: "Extended media preview"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageExtendedMediaPreview  
[Back to constructors index](/API_docs/constructors/index.html)



Extended media preview

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|w|[int](/API_docs/types/int.html) | Optional|Width|
|h|[int](/API_docs/types/int.html) | Optional|Height|
|thumb|[PhotoSize](/API_docs/types/PhotoSize.html) | Optional|Thumbnail|
|video\_duration|[int](/API_docs/types/int.html) | Optional|Video duration|



### Type: [MessageExtendedMedia](/API_docs/types/MessageExtendedMedia.html)


### Example:

```
$messageExtendedMediaPreview = ['_' => 'messageExtendedMediaPreview', 'w' => int, 'h' => int, 'thumb' => PhotoSize, 'video_duration' => int];
```  
