---
title: "inputMediaUploadedPhoto"
description: "Photo"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaUploadedPhoto  
[Back to constructors index](/API_docs/constructors/index.md)



Photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|file|[File path or InputFile](/API_docs/types/InputFile.md) | Yes|The [uploaded file](https://core.telegram.org/api/files)|
|stickers|Array of [MessageMedia, Message, Update or InputDocument](/API_docs/types/InputDocument.md) | Optional|Attached mask stickers|
|ttl\_seconds|[int](/API_docs/types/int.md) | Optional|Time to live in seconds of self-destructing photo|



### Type: [InputMedia](/API_docs/types/InputMedia.md)


### Example:

```php
$inputMediaUploadedPhoto = ['_' => 'inputMediaUploadedPhoto', 'file' => InputFile, 'stickers' => [InputDocument, InputDocument], 'ttl_seconds' => int];
```  
