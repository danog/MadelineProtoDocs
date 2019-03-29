---
title: server_DH_params_ok
description: Server params ok
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: server\_DH\_params\_ok  
[Back to constructors index](index.md)



Server params ok

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|nonce|[int128](../types/int128.md) | Yes|Random number for cryptographic security|
|server\_nonce|[int128](../types/int128.md) | Yes|Random number for cryptographic security, given by server|
|encrypted\_answer|[bytes](../types/bytes.md) | Yes|Encrypted answer|



### Type: [Server\_DH\_Params](../types/Server_DH_Params.md)


### Example:

```php
$server_DH_params_ok = ['_' => 'server_DH_params_ok', 'nonce' => int128, 'server_nonce' => int128, 'encrypted_answer' => 'bytes'];
```  


Or, if you're into Lua:

```lua
server_DH_params_ok={_='server_DH_params_ok', nonce=int128, server_nonce=int128, encrypted_answer='bytes'}

```


