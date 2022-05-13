---
title: "inputMediaUploadedDocument"
description: "New document"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaUploadedDocument  
[Back to constructors index](/API_docs/constructors/index.html)



New document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|nosound\_video|[Bool](/API_docs/types/Bool.html) | Optional|Whether the specified document is a video file with no audio tracks (a GIF animation (even as MPEG4), for example)|
|force\_file|[Bool](/API_docs/types/Bool.html) | Optional|Force the media file to be uploaded as document|
|file|[File path or InputFile](/API_docs/types/InputFile.html) | Yes|The [uploaded file](https://core.telegram.org/api/files)|
|thumb|[File path or InputFile](/API_docs/types/InputFile.html) | Optional|Thumbnail of the document, uploaded as for the file|
|mime\_type|[string](/API_docs/types/string.html) | Optional|MIME type of document|
|attributes|Array of [DocumentAttribute](/API_docs/types/DocumentAttribute.html) | Yes|Attributes that specify the type of the document (video, audio, voice, sticker, etc.)|
|stickers|Array of [MessageMedia, Message, Update or InputDocument](/API_docs/types/InputDocument.html) | Optional|Attached stickers|
|ttl\_seconds|[int](/API_docs/types/int.html) | Optional|Time to live in seconds of self-destructing document|



### Type: [InputMedia](/API_docs/types/InputMedia.html)


### Example:

```
$inputMediaUploadedDocument = ['_' => 'inputMediaUploadedDocument', 'nosound_video' => Bool, 'force_file' => Bool, 'file' => InputFile, 'thumb' => InputFile, 'mime_type' => 'string', 'attributes' => [DocumentAttribute, DocumentAttribute], 'stickers' => [InputDocument, InputDocument], 'ttl_seconds' => int];
```  
