---
title: config
description: Current configuration
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: config  
[Back to constructors index](index.md)



Current configuration

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|date|[int](../types/int.md) | Yes|Current date at the server|
|test\_mode|[Bool](../types/Bool.md) | Yes|Whether we're connected to the test DCs|
|this\_dc|[int](../types/int.md) | Yes|ID of the DC that returned the reply|
|dc\_options|Array of [DcOption](../types/DcOption.md) | Yes|DC options|
|chat\_size\_max|[int](../types/int.md) | Yes|Maximum member count for normal [groups](https://core.telegram.org/api/channel)|
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


