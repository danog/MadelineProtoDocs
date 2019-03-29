---
title: inputPhotoCrop
description: Photo crop
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPhotoCrop  
[Back to constructors index](index.md)



Photo crop

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|crop\_left|[double](../types/double.md) | Yes|Crop left|
|crop\_top|[double](../types/double.md) | Yes|Crop top|
|crop\_width|[double](../types/double.md) | Yes|Crop width|



### Type: [InputPhotoCrop](../types/InputPhotoCrop.md)


### Example:

```php
$inputPhotoCrop = ['_' => 'inputPhotoCrop', 'crop_left' => double, 'crop_top' => double, 'crop_width' => double];
```  


Or, if you're into Lua:

```lua
inputPhotoCrop={_='inputPhotoCrop', crop_left=double, crop_top=double, crop_width=double}

```


