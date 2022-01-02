---
title: "inputPhoto"
description: "Defines a photo for further interaction."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPhoto  
[Back to constructors index](index.md)



Defines a photo for further interaction.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|Photo identifier|
|access\_hash|[long](../types/long.md) | Yes|**access\_hash** value from the [photo](../constructors/photo.md) constructor|
|file\_reference|[bytes](../types/bytes.md) | Yes|[File reference](https://core.telegram.org/api/file_reference)|



### Type: [InputPhoto](../types/InputPhoto.md)


### Example:

```php
$inputPhoto = ['_' => 'inputPhoto', 'id' => long, 'access_hash' => long, 'file_reference' => 'bytes'];
```  


Or, if you're into Lua:

```lua
inputPhoto={_='inputPhoto', id=long, access_hash=long, file_reference='bytes'}

```


