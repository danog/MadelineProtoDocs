---
title: client_DH_inner_data
description: Client inner data
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: client\_DH\_inner\_data  
[Back to constructors index](index.md)



Client inner data

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|nonce|[int128](../types/int128.md) | Yes|Random number for cryptographic security|
|server\_nonce|[int128](../types/int128.md) | Yes|Random number for cryptographic security, given by server|
|retry\_id|[long](../types/long.md) | Yes|Retry ID|
|g\_b|[string](../types/string.md) | Yes|G b|



### Type: [Client\_DH\_Inner\_Data](../types/Client_DH_Inner_Data.md)


### Example:

```php
$client_DH_inner_data = ['_' => 'client_DH_inner_data', 'nonce' => int128, 'server_nonce' => int128, 'retry_id' => long, 'g_b' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "client_DH_inner_data", "nonce": int128, "server_nonce": int128, "retry_id": long, "g_b": "string"}
```


Or, if you're into Lua:

```lua
client_DH_inner_data={_='client_DH_inner_data', nonce=int128, server_nonce=int128, retry_id=long, g_b='string'}

```


