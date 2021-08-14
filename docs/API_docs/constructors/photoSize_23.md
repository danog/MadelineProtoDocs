---
title: photoSize
description: Image description.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photoSize\_23  
[Back to constructors index](index.md)



Image description.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[string](../types/string.md) | Yes|Thumbnail type|
|location|[FileLocation](../types/FileLocation.md) | Yes|File location|
|w|[int](../types/int.md) | Yes|Image width|
|h|[int](../types/int.md) | Yes|Image height|
|size|[int](../types/int.md) | Yes|File size|



### Type: [PhotoSize](../types/PhotoSize.md)


### Example:

```php
$photoSize_23 = ['_' => 'photoSize', 'type' => 'string', 'location' => FileLocation, 'w' => int, 'h' => int, 'size' => int];
```  


Or, if you're into Lua:

```lua
photoSize_23={_='photoSize', type='string', location=FileLocation, w=int, h=int, size=int}

```


