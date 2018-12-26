---
title: help.proxyDataEmpty
description: Empty proxy data
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: help.proxyDataEmpty  
[Back to constructors index](index.md)



Empty proxy data

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|expires|[int](../types/int.md) | Yes|Expires|



### Type: [help\_ProxyData](../types/help_ProxyData.md)


### Example:

```php
$help_proxyDataEmpty = ['_' => 'help.proxyDataEmpty', 'expires' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "help.proxyDataEmpty", "expires": int}
```


Or, if you're into Lua:

```lua
help_proxyDataEmpty={_='help.proxyDataEmpty', expires=int}

```


