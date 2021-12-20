---
title: "server_DH_params_ok"
description: "server_DH_params_ok attributes, type and example"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: server\_DH\_params\_ok  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|nonce|[int128](../types/int128.md) | Yes|
|server\_nonce|[int128](../types/int128.md) | Yes|
|encrypted\_answer|[string](../types/string.md) | Yes|



### Type: [Server\_DH\_Params](../types/Server_DH_Params.md)


### Example:

```php
$server_DH_params_ok = ['_' => 'server_DH_params_ok', 'nonce' => int128, 'server_nonce' => int128, 'encrypted_answer' => 'string'];
```  


Or, if you're into Lua:

```lua
server_DH_params_ok={_='server_DH_params_ok', nonce=int128, server_nonce=int128, encrypted_answer='string'}

```


