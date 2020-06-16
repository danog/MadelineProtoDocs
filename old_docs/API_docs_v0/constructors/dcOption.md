---
title: dcOption
description: Data centre
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: dcOption  
[Back to constructors index](index.md)



Data centre

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|DC ID|
|hostname|[string](../types/string.md) | Yes|
|ip\_address|[string](../types/string.md) | Yes|IP address of DC|
|port|[int](../types/int.md) | Yes|Port|



### Type: [DcOption](../types/DcOption.md)


### Example:

```php
$dcOption = ['_' => 'dcOption', 'id' => int, 'hostname' => 'string', 'ip_address' => 'string', 'port' => int];
```  


Or, if you're into Lua:

```lua
dcOption={_='dcOption', id=int, hostname='string', ip_address='string', port=int}

```


