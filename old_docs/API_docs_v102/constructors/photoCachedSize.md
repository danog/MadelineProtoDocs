---
title: photoCachedSize
description: Photo cached size
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photoCachedSize  
[Back to constructors index](index.md)



Photo cached size

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[string](../types/string.md) | Yes|Type|
|location|[FileLocation](../types/FileLocation.md) | Yes|Location|
|w|[int](../types/int.md) | Yes|Width|
|h|[int](../types/int.md) | Yes|Height|
|bytes|[bytes](../types/bytes.md) | Yes|Bytes|



### Type: [PhotoSize](../types/PhotoSize.md)


### Example:

```php
$photoCachedSize = ['_' => 'photoCachedSize', 'type' => 'string', 'location' => FileLocation, 'w' => int, 'h' => int, 'bytes' => 'bytes'];
```  


Or, if you're into Lua:

```lua
photoCachedSize={_='photoCachedSize', type='string', location=FileLocation, w=int, h=int, bytes='bytes'}

```


