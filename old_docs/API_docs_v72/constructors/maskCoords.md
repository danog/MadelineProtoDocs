---
title: maskCoords
description: Mask coords
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: maskCoords  
[Back to constructors index](index.md)



Mask coords

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|n|[int](../types/int.md) | Yes|N|
|x|[double](../types/double.md) | Yes|X|
|y|[double](../types/double.md) | Yes|Y|
|zoom|[double](../types/double.md) | Yes|Zoom|



### Type: [MaskCoords](../types/MaskCoords.md)


### Example:

```php
$maskCoords = ['_' => 'maskCoords', 'n' => int, 'x' => double, 'y' => double, 'zoom' => double];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "maskCoords", "n": int, "x": double, "y": double, "zoom": double}
```


Or, if you're into Lua:

```lua
maskCoords={_='maskCoords', n=int, x=double, y=double, zoom=double}

```


