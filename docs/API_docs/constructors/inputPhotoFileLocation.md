---
title: "inputPhotoFileLocation"
description: "Use this object to download a photo with upload.getFile method"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPhotoFileLocation  
[Back to constructors index](/API_docs/constructors/index.md)



Use this object to download a photo with [upload.getFile](../methods/upload.getFile.md) method

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.md) | Yes|Photo ID, obtained from the [photo](../constructors/photo.md) object|
|access\_hash|[long](/API_docs/types/long.md) | Yes|Photo's access hash, obtained from the [photo](../constructors/photo.md) object|
|file\_reference|[bytes](/API_docs/types/bytes.md) | Yes|[File reference](https://core.telegram.org/api/file_reference)|
|thumb\_size|[string](/API_docs/types/string.md) | Yes|The [PhotoSize](../types/PhotoSize.md) to download: must be set to the `type` field of the desired PhotoSize object of the [photo](../constructors/photo.md)|



### Type: [InputFileLocation](/API_docs/types/InputFileLocation.md)


### Example:

```php
$inputPhotoFileLocation = ['_' => 'inputPhotoFileLocation', 'id' => long, 'access_hash' => long, 'file_reference' => 'bytes', 'thumb_size' => 'string'];
```  
