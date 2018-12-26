---
title: server_DH_inner_data
description: Server inner data
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: server\_DH\_inner\_data  
[Back to constructors index](index.md)



Server inner data

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|nonce|[int128](../types/int128.md) | Yes|Random number for cryptographic security|
|server\_nonce|[int128](../types/int128.md) | Yes|Random number for cryptographic security, given by server|
|g|[int](../types/int.md) | Yes|G|
|dh\_prime|[string](../types/string.md) | Yes|Dh prime|
|g\_a|[string](../types/string.md) | Yes|G a|
|server\_time|[int](../types/int.md) | Yes|Server time|



### Type: [Server\_DH\_inner\_data](../types/Server_DH_inner_data.md)


### Example:

```php
$server_DH_inner_data = ['_' => 'server_DH_inner_data', 'nonce' => int128, 'server_nonce' => int128, 'g' => int, 'dh_prime' => 'string', 'g_a' => 'string', 'server_time' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "server_DH_inner_data", "nonce": int128, "server_nonce": int128, "g": int, "dh_prime": "string", "g_a": "string", "server_time": int}
```


Or, if you're into Lua:

```lua
server_DH_inner_data={_='server_DH_inner_data', nonce=int128, server_nonce=int128, g=int, dh_prime='string', g_a='string', server_time=int}

```


