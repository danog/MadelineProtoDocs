---
title: dcOption
description: DC option
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: dcOption  
[Back to constructors index](index.md)



DC option

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|ipv6|[Bool](../types/Bool.md) | Optional|Ipv6?|
|media\_only|[Bool](../types/Bool.md) | Optional|Media only?|
|tcpo\_only|[Bool](../types/Bool.md) | Optional|Tcpo only?|
|id|[int](../types/int.md) | Yes|ID|
|ip\_address|[string](../types/string.md) | Yes|Ip address|
|port|[int](../types/int.md) | Yes|Port|



### Type: [DcOption](../types/DcOption.md)


### Example:

```php
$dcOption = ['_' => 'dcOption', 'ipv6' => Bool, 'media_only' => Bool, 'tcpo_only' => Bool, 'id' => int, 'ip_address' => 'string', 'port' => int];
```  


Or, if you're into Lua:

```lua
dcOption={_='dcOption', ipv6=Bool, media_only=Bool, tcpo_only=Bool, id=int, ip_address='string', port=int}

```


