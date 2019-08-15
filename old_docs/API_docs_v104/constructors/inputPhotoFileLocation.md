---
title: inputPhotoFileLocation
description: Photo file location
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPhotoFileLocation  
[Back to constructors index](index.md)



Photo file location

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|file\_reference|[bytes](../types/bytes.md) | Yes|File reference|
|thumb\_size|[string](../types/string.md) | Yes|Thumb size|



### Type: [InputFileLocation](../types/InputFileLocation.md)


### Example:

```php
$inputPhotoFileLocation = ['_' => 'inputPhotoFileLocation', 'id' => long, 'access_hash' => long, 'file_reference' => 'bytes', 'thumb_size' => 'string'];
```  


Or, if you're into Lua:

```lua
inputPhotoFileLocation={_='inputPhotoFileLocation', id=long, access_hash=long, file_reference='bytes', thumb_size='string'}

```


