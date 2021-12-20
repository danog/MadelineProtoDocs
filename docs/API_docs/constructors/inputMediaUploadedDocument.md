---
title: "inputMediaUploadedDocument"
description: "New document"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaUploadedDocument  
[Back to constructors index](index.md)



New document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|nosound\_video|[Bool](../types/Bool.md) | Optional|Whether the specified document is a video file with no audio tracks (a GIF animation (even as MPEG4), for example)|
|force\_file|[Bool](../types/Bool.md) | Optional|Force the media file to be uploaded as document|
|file|[File path or InputFile](../types/InputFile.md) | Yes|The [uploaded file](https://core.telegram.org/api/files)|
|thumb|[File path or InputFile](../types/InputFile.md) | Optional|Thumbnail of the document, uploaded as for the file|
|mime\_type|[string](../types/string.md) | Optional|MIME type of document|
|attributes|Array of [DocumentAttribute](../types/DocumentAttribute.md) | Yes|Attributes that specify the type of the document (video, audio, voice, sticker, etc.)|
|stickers|Array of [MessageMedia, Message, Update or InputDocument](../types/InputDocument.md) | Optional|Attached stickers|
|ttl\_seconds|[int](../types/int.md) | Optional|Time to live in seconds of self-destructing document|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaUploadedDocument = ['_' => 'inputMediaUploadedDocument', 'nosound_video' => Bool, 'force_file' => Bool, 'file' => InputFile, 'thumb' => InputFile, 'mime_type' => 'string', 'attributes' => [DocumentAttribute, DocumentAttribute], 'stickers' => [InputDocument, InputDocument], 'ttl_seconds' => int];
```  


Or, if you're into Lua:

```lua
inputMediaUploadedDocument={_='inputMediaUploadedDocument', nosound_video=Bool, force_file=Bool, file=InputFile, thumb=InputFile, mime_type='string', attributes={DocumentAttribute}, stickers={InputDocument}, ttl_seconds=int}

```


