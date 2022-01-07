---
title: "auth.bindTempAuthKey"
description: "You cannot use this method directly, instead modify the PFS and default_temp_auth_key_expires_in settings, see https://docs.madelineproto.xyz/docs/SETTINGS.html for more info"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_bindTempAuthKey.html
---
# Method: auth.bindTempAuthKey
[Back to methods index](index.md)



You cannot use this method directly, instead modify the PFS and default_temp_auth_key_expires_in settings, see https://docs.madelineproto.xyz/docs/SETTINGS.html for more info

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

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|ENCRYPTED_MESSAGE_INVALID|Encrypted message invalid|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|
|400|INPUT_REQUEST_TOO_LONG|The request is too big|
|400|TEMP_AUTH_KEY_EMPTY|No temporary auth key provided|
|-500|No workers running|Internal error|
|-503|Timeout|Timeout while fetching data|


