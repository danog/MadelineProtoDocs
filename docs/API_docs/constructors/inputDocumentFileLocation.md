---
title: "inputDocumentFileLocation"
description: "Document location (video, voice, audio, basically every type except photo)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputDocumentFileLocation  
[Back to constructors index](/API_docs/constructors/index.md)



Document location (video, voice, audio, basically every type except photo)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.md) | Yes|Document ID|
|access\_hash|[long](/API_docs/types/long.md) | Yes|**access\_hash** parameter from the [document](../constructors/document.md) constructor|
|file\_reference|[bytes](/API_docs/types/bytes.md) | Yes|[File reference](https://core.telegram.org/api/file_reference)|
|thumb\_size|[string](/API_docs/types/string.md) | Yes|Thumbnail size to download the thumbnail|



### Type: [InputFileLocation](/API_docs/types/InputFileLocation.md)


### Example:

```php
$inputDocumentFileLocation = ['_' => 'inputDocumentFileLocation', 'id' => long, 'access_hash' => long, 'file_reference' => 'bytes', 'thumb_size' => 'string'];
```  
