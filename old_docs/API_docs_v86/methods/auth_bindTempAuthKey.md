---
title: auth.bindTempAuthKey
description: You cannot use this method directly, instead modify the PFS and default_temp_auth_key_expires_in settings, see https://docs.madelineproto.xyz/docs/SETTINGS.html for more info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: auth.bindTempAuthKey  
[Back to methods index](index.md)


You cannot use this method directly, instead modify the PFS and default_temp_auth_key_expires_in settings, see https://docs.madelineproto.xyz/docs/SETTINGS.html for more info

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|perm\_auth\_key\_id|[long](../types/long.md) | You cannot use this method directly, instead modify the PFS and default_temp_auth_key_expires_in settings, see https://docs.madelineproto.xyz/docs/SETTINGS.html for more info | Yes|
|nonce|[long](../types/long.md) | You cannot use this method directly, instead modify the PFS and default_temp_auth_key_expires_in settings, see https://docs.madelineproto.xyz/docs/SETTINGS.html for more info | Yes|
|expires\_at|[int](../types/int.md) | You cannot use this method directly, instead modify the PFS and default_temp_auth_key_expires_in settings, see https://docs.madelineproto.xyz/docs/SETTINGS.html for more info | Yes|
|encrypted\_message|[bytes](../types/bytes.md) | You cannot use this method directly, instead modify the PFS and default_temp_auth_key_expires_in settings, see https://docs.madelineproto.xyz/docs/SETTINGS.html for more info | Yes|


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
|400|INPUT_REQUEST_TOO_LONG|The request is too big|
|400|TEMP_AUTH_KEY_EMPTY|No temporary auth key provided|
|-503|Timeout|Timeout while fetching data|


