---
title: nearestDc
description: Nearest data centre, according to geo-ip.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: nearestDc  
[Back to constructors index](index.md)



Nearest data centre, according to geo-ip.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|country|[string](../types/string.md) | Yes|Country code determined by geo-ip|
|this\_dc|[int](../types/int.md) | Yes|Number of current data centre|
|nearest\_dc|[int](../types/int.md) | Yes|Number of nearest data centre|



### Type: [NearestDc](../types/NearestDc.md)


### Example:

```php
$nearestDc = ['_' => 'nearestDc', 'country' => 'string', 'this_dc' => int, 'nearest_dc' => int];
```  


Or, if you're into Lua:

```lua
nearestDc={_='nearestDc', country='string', this_dc=int, nearest_dc=int}

```


