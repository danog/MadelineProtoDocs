---
title: config
description: Config
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: config  
[Back to constructors index](index.md)



Config

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|date|[int](../types/int.md) | Yes|Date|
|test\_mode|[Bool](../types/Bool.md) | Yes|Test mode?|
|this\_dc|[int](../types/int.md) | Yes|This DC|
|dc\_options|Array of [DcOption](../types/DcOption.md) | Yes|DC options|
|chat\_size\_max|[int](../types/int.md) | Yes|Chat size max|
|broadcast\_size\_max|[int](../types/int.md) | Yes|Broadcast size max|



### Type: [Config](../types/Config.md)


### Example:

```php
$config = ['_' => 'config', 'date' => int, 'test_mode' => Bool, 'this_dc' => int, 'dc_options' => [DcOption, DcOption], 'chat_size_max' => int, 'broadcast_size_max' => int];
```  


Or, if you're into Lua:

```lua
config={_='config', date=int, test_mode=Bool, this_dc=int, dc_options={DcOption}, chat_size_max=int, broadcast_size_max=int}

```


