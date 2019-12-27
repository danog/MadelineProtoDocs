---
title: inputMediaUploadedDocument
description: New document
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaUploadedDocument  
[Back to constructors index](index.md)



New document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|file|[File path or InputFile](../types/InputFile.md) | Yes|The [uploaded file](https://core.telegram.org/api/files)|
|file\_name|[string](../types/string.md) | Yes|File name|
|mime\_type|[string](../types/string.md) | Optional|MIME type of document|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaUploadedDocument = ['_' => 'inputMediaUploadedDocument', 'file' => InputFile, 'file_name' => 'string', 'mime_type' => 'string'];
```  


Or, if you're into Lua:

```lua
inputMediaUploadedDocument={_='inputMediaUploadedDocument', file=InputFile, file_name='string', mime_type='string'}

```


