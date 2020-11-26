---
title: maskCoords
description: Position on a photo where a mask should be placed
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: maskCoords  
[Back to constructors index](index.md)



Position on a photo where a mask should be placed

The `n` position indicates where the mask should be placed:

- 0 =&gt; Relative to the forehead
- 1 =&gt; Relative to the eyes
- 2 =&gt; Relative to the mouth
- 3 =&gt; Relative to the chin

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|n|[int](../types/int.md) | Yes|Part of the face, relative to which the mask should be placed|
|x|[double](../types/double.md) | Yes|Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. (For example, -1.0 will place the mask just to the left of the default mask position)|
|y|[double](../types/double.md) | Yes|Shift by Y-axis measured in widths of the mask scaled to the face size, from left to right. (For example, -1.0 will place the mask just to the left of the default mask position)|
|zoom|[double](../types/double.md) | Yes|Mask scaling coefficient. (For example, 2.0 means a doubled size)|



### Type: [MaskCoords](../types/MaskCoords.md)


### Example:

```php
$maskCoords = ['_' => 'maskCoords', 'n' => int, 'x' => double, 'y' => double, 'zoom' => double];
```  


Or, if you're into Lua:

```lua
maskCoords={_='maskCoords', n=int, x=double, y=double, zoom=double}

```


