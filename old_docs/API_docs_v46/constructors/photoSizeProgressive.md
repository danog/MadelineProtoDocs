---
title: photoSizeProgressive
description: photoSizeProgressive attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photoSizeProgressive  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|type|[string](../types/string.md) | Yes|
|location|[FileLocation](../types/FileLocation.md) | Yes|
|w|[int](../types/int.md) | Yes|
|h|[int](../types/int.md) | Yes|
|sizes|Array of [int](../types/int.md) | Yes|



### Type: [PhotoSize](../types/PhotoSize.md)


### Example:

```php
$photoSizeProgressive = ['_' => 'photoSizeProgressive', 'type' => 'string', 'location' => FileLocation, 'w' => int, 'h' => int, 'sizes' => [int, int]];
```  


Or, if you're into Lua:

```lua
photoSizeProgressive={_='photoSizeProgressive', type='string', location=FileLocation, w=int, h=int, sizes={int}}

```


