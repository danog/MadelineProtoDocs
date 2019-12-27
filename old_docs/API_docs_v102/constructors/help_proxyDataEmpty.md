---
title: help.proxyDataEmpty
description: No proxy was used to connect to tg (or none was provided to [initConnection](../methods/initConnection.md), or the used proxy doesn't have a promotion channel associated to it)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: help.proxyDataEmpty  
[Back to constructors index](index.md)



No proxy was used to connect to tg (or none was provided to [initConnection](../methods/initConnection.md), or the used proxy doesn't have a promotion channel associated to it)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|expires|[int](../types/int.md) | Yes|Expiration date of proxy info, will have to be refetched in `expires` seconds|



### Type: [help\_ProxyData](../types/help_ProxyData.md)


### Example:

```php
$help_proxyDataEmpty = ['_' => 'help.proxyDataEmpty', 'expires' => int];
```  


Or, if you're into Lua:

```lua
help_proxyDataEmpty={_='help.proxyDataEmpty', expires=int}

```


