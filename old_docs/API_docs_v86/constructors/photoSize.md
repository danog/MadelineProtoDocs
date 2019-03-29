---
title: photoSize
description: Photo size
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photoSize  
[Back to constructors index](index.md)



Photo size

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[string](../types/string.md) | Yes|Type|
|location|[FileLocation](../types/FileLocation.md) | Yes|Location|
|w|[int](../types/int.md) | Yes|Width|
|h|[int](../types/int.md) | Yes|Height|
|size|[int](../types/int.md) | Yes|Size|



### Type: [PhotoSize](../types/PhotoSize.md)


### Example:

```php
$photoSize = ['_' => 'photoSize', 'type' => 'string', 'location' => FileLocation, 'w' => int, 'h' => int, 'size' => int];
```  


Or, if you're into Lua:

```lua
photoSize={_='photoSize', type='string', location=FileLocation, w=int, h=int, size=int}

```


