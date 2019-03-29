---
title: p_q_inner_data_temp
description: Inner data temp
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: p\_q\_inner\_data\_temp  
[Back to constructors index](index.md)



Inner data temp

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pq|[bytes](../types/bytes.md) | Yes|Pq|
|p|[bytes](../types/bytes.md) | Yes|P|
|q|[bytes](../types/bytes.md) | Yes|Q|
|nonce|[int128](../types/int128.md) | Yes|Random number for cryptographic security|
|server\_nonce|[int128](../types/int128.md) | Yes|Random number for cryptographic security, given by server|
|new\_nonce|[int256](../types/int256.md) | Yes|New nonce|
|expires\_in|[int](../types/int.md) | Yes|Expires in|



### Type: [P\_Q\_inner\_data](../types/P_Q_inner_data.md)


### Example:

```php
$p_q_inner_data_temp = ['_' => 'p_q_inner_data_temp', 'pq' => 'bytes', 'p' => 'bytes', 'q' => 'bytes', 'nonce' => int128, 'server_nonce' => int128, 'new_nonce' => int256, 'expires_in' => int];
```  


Or, if you're into Lua:

```lua
p_q_inner_data_temp={_='p_q_inner_data_temp', pq='bytes', p='bytes', q='bytes', nonce=int128, server_nonce=int128, new_nonce=int256, expires_in=int}

```


