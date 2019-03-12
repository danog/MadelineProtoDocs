---
title: req_DH_params
description: Requests Diffie-hellman parameters for key exchange
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: req\_DH\_params  
[Back to methods index](index.md)


Requests Diffie-hellman parameters for key exchange

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|nonce|[int128](../types/int128.md) | Random number for cryptographic security | Yes|
|server\_nonce|[int128](../types/int128.md) | Random number for cryptographic security, given by server | Yes|
|p|[string](../types/string.md) | Factorized p from pq | Yes|
|q|[string](../types/string.md) | Factorized q from pq | Yes|
|public\_key\_fingerprint|[long](../types/long.md) | Server RSA fingerprint | Yes|
|encrypted\_data|[string](../types/string.md) | Encrypted message | Yes|


### Return type: [Server\_DH\_Params](../types/Server_DH_Params.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Server_DH_Params = $MadelineProto->req_DH_params(['nonce' => int128, 'server_nonce' => int128, 'p' => 'string', 'q' => 'string', 'public_key_fingerprint' => long, 'encrypted_data' => 'string', ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - req_DH_params
* params - `{"nonce": int128, "server_nonce": int128, "p": "string", "q": "string", "public_key_fingerprint": long, "encrypted_data": "string", }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/req_DH_params`

Parameters:

nonce - Json encoded int128

server_nonce - Json encoded int128

p - Json encoded string

q - Json encoded string

public_key_fingerprint - Json encoded long

encrypted_data - Json encoded string




Or, if you're into Lua:

```lua
Server_DH_Params = req_DH_params({nonce=int128, server_nonce=int128, p='string', q='string', public_key_fingerprint=long, encrypted_data='string', })
```

