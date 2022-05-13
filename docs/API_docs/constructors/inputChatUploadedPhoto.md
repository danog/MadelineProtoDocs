---
title: "inputChatUploadedPhoto"
description: "New photo to be set as group profile photo."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputChatUploadedPhoto  
[Back to constructors index](/API_docs/constructors/index.html)



New photo to be set as group profile photo.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|file|[File path or InputFile](/API_docs/types/InputFile.html) | Optional|File saved in parts using the method [upload.saveFilePart](../methods/upload.saveFilePart.html)|
|video|[File path or InputFile](/API_docs/types/InputFile.html) | Optional|Square video for animated profile picture|
|video\_start\_ts|[double](/API_docs/types/double.html) | Optional|Timestamp that should be shown as static preview to the user (seconds)|



### Type: [InputChatPhoto](/API_docs/types/InputChatPhoto.html)


### Example:

```
$inputChatUploadedPhoto = ['_' => 'inputChatUploadedPhoto', 'file' => InputFile, 'video' => InputFile, 'video_start_ts' => double];
```  
