---
title: documentAttributeImageSize
description: documentAttributeImageSize attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeImageSize  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|w|[int](../types/int.md) | Optional|
|h|[int](../types/int.md) | Optional|



### Type: [DocumentAttribute](../types/DocumentAttribute.md)


### Example:

```php
$documentAttributeImageSize = ['_' => 'documentAttributeImageSize', 'w' => int, 'h' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "documentAttributeImageSize", "w": int, "h": int}
```


Or, if you're into Lua:

```lua
documentAttributeImageSize={_='documentAttributeImageSize', w=int, h=int}

```


