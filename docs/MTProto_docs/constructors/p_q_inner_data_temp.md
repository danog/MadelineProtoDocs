---
title: p_q_inner_data_temp
description: p_q_inner_data_temp attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: p\_q\_inner\_data\_temp  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|pq|[string](../types/string.md) | Yes|
|p|[string](../types/string.md) | Yes|
|q|[string](../types/string.md) | Yes|
|nonce|[int128](../types/int128.md) | Yes|
|server\_nonce|[int128](../types/int128.md) | Yes|
|new\_nonce|[int256](../types/int256.md) | Yes|
|expires\_in|[int](../types/int.md) | Yes|



### Type: [P\_Q\_inner\_data](../types/P_Q_inner_data.md)


### Example:

```php
$p_q_inner_data_temp = ['_' => 'p_q_inner_data_temp', 'pq' => 'string', 'p' => 'string', 'q' => 'string', 'nonce' => int128, 'server_nonce' => int128, 'new_nonce' => int256, 'expires_in' => int];
```  


Or, if you're into Lua:

```lua
p_q_inner_data_temp={_='p_q_inner_data_temp', pq='string', p='string', q='string', nonce=int128, server_nonce=int128, new_nonce=int256, expires_in=int}

```


