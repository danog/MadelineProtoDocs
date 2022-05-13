---
title: "inputPhotoFileLocation"
description: "Use this object to download a photo with upload.getFile method"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPhotoFileLocation  
[Back to constructors index](/API_docs/constructors/index.html)



Use this object to download a photo with [upload.getFile](../methods/upload.getFile.html) method

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|Photo ID, obtained from the [photo](../constructors/photo.html) object|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Photo's access hash, obtained from the [photo](../constructors/photo.html) object|
|file\_reference|[bytes](/API_docs/types/bytes.html) | Yes|[File reference](https://core.telegram.org/api/file_reference)|
|thumb\_size|[string](/API_docs/types/string.html) | Yes|The [PhotoSize](../types/PhotoSize.html) to download: must be set to the `type` field of the desired PhotoSize object of the [photo](../constructors/photo.html)|



### Type: [InputFileLocation](/API_docs/types/InputFileLocation.html)


### Example:

```
$inputPhotoFileLocation = ['_' => 'inputPhotoFileLocation', 'id' => long, 'access_hash' => long, 'file_reference' => 'bytes', 'thumb_size' => 'string'];
```  
