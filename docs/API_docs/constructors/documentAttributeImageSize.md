---
title: "documentAttributeImageSize"
description: "Defines the width and height of an image uploaded as document"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeImageSize  
[Back to constructors index](index.md)



Defines the width and height of an image uploaded as document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|w|[int](../types/int.md) | Optional|Width of image|
|h|[int](../types/int.md) | Optional|Height of image|



### Type: [DocumentAttribute](../types/DocumentAttribute.md)


### Example:

```php
$documentAttributeImageSize = ['_' => 'documentAttributeImageSize', 'w' => int, 'h' => int];
```  


Or, if you're into Lua:

```lua
documentAttributeImageSize={_='documentAttributeImageSize', w=int, h=int}

```


