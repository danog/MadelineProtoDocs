---
title: nearestDc
description: Nearest DC
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: nearestDc  
[Back to constructors index](index.md)



Nearest DC

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|country|[string](../types/string.md) | Yes|Country|
|this\_dc|[int](../types/int.md) | Yes|This DC|
|nearest\_dc|[int](../types/int.md) | Yes|Nearest DC|



### Type: [NearestDc](../types/NearestDc.md)


### Example:

```php
$nearestDc = ['_' => 'nearestDc', 'country' => 'string', 'this_dc' => int, 'nearest_dc' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "nearestDc", "country": "string", "this_dc": int, "nearest_dc": int}
```


Or, if you're into Lua:

```lua
nearestDc={_='nearestDc', country='string', this_dc=int, nearest_dc=int}

```


