---
title: "auth.bindTempAuthKey"
description: "Binds a temporary authorization key `temp_auth_key_id` to the permanent authorization key `perm_auth_key_id`. Each permanent key may only be bound to one temporary key at a time, binding a new temporary key overwrites the previous one."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_bindTempAuthKey.html
---
# Method: auth.bindTempAuthKey
[Back to methods index](index.md)



Binds a temporary authorization key `temp_auth_key_id` to the permanent authorization key `perm_auth_key_id`. Each permanent key may only be bound to one temporary key at a time, binding a new temporary key overwrites the previous one.

For more information, see [Perfect Forward Secrecy](https://core.telegram.org/api/pfs).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|perm\_auth\_key\_id|[long](../types/long.md) | Permanent auth\_key\_id to bind to | Yes|
|nonce|[long](../types/long.md) | Random long from [Binding message contents](#binding-message-contents) | Yes|
|expires\_at|[int](../types/int.md) | Unix timestamp to invalidate temporary key, see [Binding message contents](#binding-message-contents) | Yes|
|encrypted\_message|[bytes](../types/bytes.md) | See [Generating encrypted\_message](#generating-encrypted-message) | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->auth->bindTempAuthKey(['perm_auth_key_id' => long, 'nonce' => long, 'expires_at' => int, 'encrypted_message' => 'bytes', ]);
```

Or, if you're into Lua:

```lua
Bool = auth.bindTempAuthKey({perm_auth_key_id=long, nonce=long, expires_at=int, encrypted_message='bytes', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|ENCRYPTED_MESSAGE_INVALID|Encrypted message invalid|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|
|400|INPUT_REQUEST_TOO_LONG|The request is too big|
|400|TEMP_AUTH_KEY_EMPTY|No temporary auth key provided|
|-500|No workers running|Internal error|
|-503|Timeout|Timeout while fetching data|


