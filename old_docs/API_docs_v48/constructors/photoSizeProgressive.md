---
title: photoSizeProgressive
description: Progressively encoded photosize
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photoSizeProgressive  
[Back to constructors index](index.md)



Progressively encoded photosize

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[string](../types/string.md) | Yes|Photosize type|
|w|[int](../types/int.md) | Yes|Photo width|
|h|[int](../types/int.md) | Yes|Photo height|
|sizes|Array of [int](../types/int.md) | Yes|Sizes of progressive JPEG file prefixes, which can be used to preliminarily show the image.|



### Type: [PhotoSize](../types/PhotoSize.md)


### Example:

```php
$photoSizeProgressive = ['_' => 'photoSizeProgressive', 'type' => 'string', 'w' => int, 'h' => int, 'sizes' => [int, int]];
```  


Or, if you're into Lua:

```lua
photoSizeProgressive={_='photoSizeProgressive', type='string', w=int, h=int, sizes={int}}

```


