---
title: resPQ
description: Contains pq to factorize
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: resPQ  
[Back to constructors index](index.md)



Contains pq to factorize

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|nonce|[int128](../types/int128.md) | Yes|Nonce|
|server\_nonce|[int128](../types/int128.md) | Yes|Server nonce|
|pq|[string](../types/string.md) | Yes|Pq|
|server\_public\_key\_fingerprints|Array of [long](../types/long.md) | Yes|RSA key fingerprints|



### Type: [ResPQ](../types/ResPQ.md)


### Example:

```php
$resPQ = ['_' => 'resPQ', 'nonce' => int128, 'server_nonce' => int128, 'pq' => 'string', 'server_public_key_fingerprints' => [long, long]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "resPQ", "nonce": int128, "server_nonce": int128, "pq": "string", "server_public_key_fingerprints": [long]}
```


Or, if you're into Lua:

```lua
resPQ={_='resPQ', nonce=int128, server_nonce=int128, pq='string', server_public_key_fingerprints={long}}

```


