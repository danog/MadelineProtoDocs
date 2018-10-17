---
title: photoSize
description: photoSize attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photoSize  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|type|[string](../types/string.md) | Yes|
|location|[FileLocation](../types/FileLocation.md) | Yes|
|w|[int](../types/int.md) | Yes|
|h|[int](../types/int.md) | Yes|
|size|[int](../types/int.md) | Yes|



### Type: [PhotoSize](../types/PhotoSize.md)


### Example:

```php
$photoSize = ['_' => 'photoSize', 'type' => 'string', 'location' => FileLocation, 'w' => int, 'h' => int, 'size' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "photoSize", "type": "string", "location": FileLocation, "w": int, "h": int, "size": int}
```


Or, if you're into Lua:

```lua
photoSize={_='photoSize', type='string', location=FileLocation, w=int, h=int, size=int}

```


