---
title: set_client_DH_params
description: Sets client diffie-hellman parameters
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: set\_client\_DH\_params  
[Back to methods index](index.md)


Sets client diffie-hellman parameters

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|nonce|[int128](../types/int128.md) | Random number for cryptographic security | Yes|
|server\_nonce|[int128](../types/int128.md) | Random number for cryptographic security, given by server | Yes|
|encrypted\_data|[bytes](../types/bytes.md) | Encrypted key exchange message | Yes|


### Return type: [Set\_client\_DH\_params\_answer](../types/Set_client_DH_params_answer.md)

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

$Set_client_DH_params_answer = $MadelineProto->set_client_DH_params(['nonce' => int128, 'server_nonce' => int128, 'encrypted_data' => 'bytes', ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - set_client_DH_params
* params - `{"nonce": int128, "server_nonce": int128, "encrypted_data": {"_": "bytes", "bytes":"base64 encoded bytes"}, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/set_client_DH_params`

Parameters:

nonce - Json encoded int128

server_nonce - Json encoded int128

encrypted_data - Json encoded bytes




Or, if you're into Lua:

```lua
Set_client_DH_params_answer = set_client_DH_params({nonce=int128, server_nonce=int128, encrypted_data='bytes', })
```

