---
title: inputMediaUploadedThumbDocument
description: Media uploaded thumb document
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaUploadedThumbDocument  
[Back to constructors index](index.md)



Media uploaded thumb document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|file|[File path or InputFile](../types/InputFile.md) | Yes|File|
|thumb|[File path or InputFile](../types/InputFile.md) | Yes|Thumbnail|
|mime\_type|[string](../types/string.md) | Optional|Mime type|
|attributes|Array of [DocumentAttribute](../types/DocumentAttribute.md) | Yes|Attributes|
|caption|[string](../types/string.md) | Yes|Caption|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaUploadedThumbDocument = ['_' => 'inputMediaUploadedThumbDocument', 'file' => InputFile, 'thumb' => InputFile, 'mime_type' => 'string', 'attributes' => [DocumentAttribute, DocumentAttribute], 'caption' => 'string'];
```  


Or, if you're into Lua:

```lua
inputMediaUploadedThumbDocument={_='inputMediaUploadedThumbDocument', file=InputFile, thumb=InputFile, mime_type='string', attributes={DocumentAttribute}, caption='string'}

```


