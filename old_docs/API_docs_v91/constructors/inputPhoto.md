---
title: inputPhoto
description: Photo
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPhoto  
[Back to constructors index](index.md)



Photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|file\_reference|[bytes](../types/bytes.md) | Yes|File reference|



### Type: [InputPhoto](../types/InputPhoto.md)


### Example:

```php
$inputPhoto = ['_' => 'inputPhoto', 'id' => long, 'access_hash' => long, 'file_reference' => 'bytes'];
```  


Or, if you're into Lua:

```lua
inputPhoto={_='inputPhoto', id=long, access_hash=long, file_reference='bytes'}

```


