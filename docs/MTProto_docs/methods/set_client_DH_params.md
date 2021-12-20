---
title: "set_client_DH_params"
description: "set_client_DH_params parameters, return type and example"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: set\_client\_DH\_params
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|nonce|[int128](../types/int128.md) | Yes|
|server\_nonce|[int128](../types/int128.md) | Yes|
|encrypted\_data|[string](../types/string.md) | Yes|


### Return type: [Set\_client\_DH\_params\_answer](../types/Set_client_DH_params_answer.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Set_client_DH_params_answer = $MadelineProto->set_client_DH_params(['nonce' => int128, 'server_nonce' => int128, 'encrypted_data' => 'string', ]);
```

Or, if you're into Lua:

```lua
Set_client_DH_params_answer = set_client_DH_params({nonce=int128, server_nonce=int128, encrypted_data='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|UNKNOWN_ERROR|Internal error|


