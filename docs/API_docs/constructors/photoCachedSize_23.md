---
title: photoCachedSize
description: Description of an image and its content.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photoCachedSize\_23  
[Back to constructors index](index.md)



Description of an image and its content.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[string](../types/string.md) | Yes|Thumbnail type|
|location|[FileLocation](../types/FileLocation.md) | Yes|File location|
|w|[int](../types/int.md) | Yes|Image width|
|h|[int](../types/int.md) | Yes|Image height|
|bytes|[bytes](../types/bytes.md) | Yes|Binary data, file content|



### Type: [PhotoSize](../types/PhotoSize.md)


### Example:

```php
$photoCachedSize_23 = ['_' => 'photoCachedSize', 'type' => 'string', 'location' => FileLocation, 'w' => int, 'h' => int, 'bytes' => 'bytes'];
```  


Or, if you're into Lua:

```lua
photoCachedSize_23={_='photoCachedSize', type='string', location=FileLocation, w=int, h=int, bytes='bytes'}

```


