---
title: p_q_inner_data
description: PQ inner data
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: p\_q\_inner\_data  
[Back to constructors index](index.md)



PQ inner data

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pq|[string](../types/string.md) | Yes||
|p|[string](../types/string.md) | Yes||
|q|[string](../types/string.md) | Yes||
|nonce|[int128](../types/int128.md) | Yes|Nonce|
|server\_nonce|[int128](../types/int128.md) | Yes|Nonce|
|new\_nonce|[int256](../types/int256.md) | Yes|Nonce|



### Type: [P\_Q\_inner\_data](../types/P_Q_inner_data.md)


### Example:

```php
$p_q_inner_data = ['_' => 'p_q_inner_data', 'pq' => 'string', 'p' => 'string', 'q' => 'string', 'nonce' => int128, 'server_nonce' => int128, 'new_nonce' => int256];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "p_q_inner_data", "pq": "string", "p": "string", "q": "string", "nonce": int128, "server_nonce": int128, "new_nonce": int256}
```


Or, if you're into Lua:

```lua
p_q_inner_data={_='p_q_inner_data', pq='string', p='string', q='string', nonce=int128, server_nonce=int128, new_nonce=int256}

```


