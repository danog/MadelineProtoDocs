---
title: inputPhotoLegacyFileLocation
description: Legacy photo file location
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPhotoLegacyFileLocation  
[Back to constructors index](index.md)



Legacy photo file location

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|Photo ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|file\_reference|[bytes](../types/bytes.md) | Yes|File reference|
|volume\_id|[long](../types/long.md) | Yes|Volume ID|
|local\_id|[int](../types/int.md) | Yes|Local ID|
|secret|[long](../types/long.md) | Yes|Secret|



### Type: [InputFileLocation](../types/InputFileLocation.md)


### Example:

```php
$inputPhotoLegacyFileLocation = ['_' => 'inputPhotoLegacyFileLocation', 'id' => long, 'access_hash' => long, 'file_reference' => 'bytes', 'volume_id' => long, 'local_id' => int, 'secret' => long];
```  


Or, if you're into Lua:

```lua
inputPhotoLegacyFileLocation={_='inputPhotoLegacyFileLocation', id=long, access_hash=long, file_reference='bytes', volume_id=long, local_id=int, secret=long}

```


