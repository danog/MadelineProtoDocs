---
title: "inputChatUploadedPhoto"
description: "New photo to be set as group profile photo."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputChatUploadedPhoto  
[Back to constructors index](index.md)



New photo to be set as group profile photo.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|file|[File path or InputFile](../types/InputFile.md) | Optional|File saved in parts using the method [upload.saveFilePart](../methods/upload.saveFilePart.md)|
|video|[File path or InputFile](../types/InputFile.md) | Optional|Square video for animated profile picture|
|video\_start\_ts|[double](../types/double.md) | Optional|Timestamp that should be shown as static preview to the user (seconds)|



### Type: [InputChatPhoto](../types/InputChatPhoto.md)


### Example:

```php
$inputChatUploadedPhoto = ['_' => 'inputChatUploadedPhoto', 'file' => InputFile, 'video' => InputFile, 'video_start_ts' => double];
```  
