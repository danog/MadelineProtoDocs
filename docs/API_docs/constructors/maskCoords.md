---
title: "maskCoords"
description: "Position on a photo where a mask should be placed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: maskCoords  
[Back to constructors index](/API_docs/constructors/index.html)



Position on a photo where a mask should be placed

The `n` position indicates where the mask should be placed:

- 0 =&gt; Relative to the forehead
- 1 =&gt; Relative to the eyes
- 2 =&gt; Relative to the mouth
- 3 =&gt; Relative to the chin

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|n|[int](/API_docs/types/int.html) | Yes|Part of the face, relative to which the mask should be placed|
|x|[double](/API_docs/types/double.html) | Yes|Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. (For example, -1.0 will place the mask just to the left of the default mask position)|
|y|[double](/API_docs/types/double.html) | Yes|Shift by Y-axis measured in widths of the mask scaled to the face size, from left to right. (For example, -1.0 will place the mask just to the left of the default mask position)|
|zoom|[double](/API_docs/types/double.html) | Yes|Mask scaling coefficient. (For example, 2.0 means a doubled size)|



### Type: [MaskCoords](/API_docs/types/MaskCoords.html)


### Example:

```
$maskCoords = ['_' => 'maskCoords', 'n' => int, 'x' => double, 'y' => double, 'zoom' => double];
```  
