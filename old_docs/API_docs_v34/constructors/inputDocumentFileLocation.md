---
title: inputDocumentFileLocation
description: Document location (video, voice, audio, basically every type except photo)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputDocumentFileLocation  
[Back to constructors index](index.md)



Document location (video, voice, audio, basically every type except photo)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|Document ID|
|access\_hash|[long](../types/long.md) | Yes|**access\_hash** parameter from the [document](../constructors/document.md) constructor|
|file\_reference|[bytes](../types/bytes.md) | Yes|[File reference](https://core.telegram.org/api/file_reference)|
|thumb\_size|[string](../types/string.md) | Yes|Thumbnail size to download the thumbnail|



### Type: [InputFileLocation](../types/InputFileLocation.md)


### Example:

```php
$inputDocumentFileLocation = ['_' => 'inputDocumentFileLocation', 'id' => long, 'access_hash' => long, 'file_reference' => 'bytes', 'thumb_size' => 'string'];
```  


Or, if you're into Lua:

```lua
inputDocumentFileLocation={_='inputDocumentFileLocation', id=long, access_hash=long, file_reference='bytes', thumb_size='string'}

```


