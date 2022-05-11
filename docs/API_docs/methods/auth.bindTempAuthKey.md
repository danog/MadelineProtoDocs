---
title: "auth.bindTempAuthKey"
description: "You cannot use this method directly, instead modify the PFS and default_temp_auth_key_expires_in settings, see https://docs.madelineproto.xyz/docs/SETTINGS.html for more info"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_bindTempAuthKey.html
---
# Method: auth.bindTempAuthKey
[Back to methods index](index.html)



You cannot use this method directly, instead modify the PFS and default_temp_auth_key_expires_in settings, see https://docs.madelineproto.xyz/docs/SETTINGS.html for more info

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|perm\_auth\_key\_id|[long](/API_docs/types/long.html) | Permanent auth\_key\_id to bind to | Yes|
|nonce|[long](/API_docs/types/long.html) | Random long from [Binding message contents](#binding-message-contents) | Yes|
|expires\_at|[int](/API_docs/types/int.html) | Unix timestamp to invalidate temporary key, see [Binding message contents](#binding-message-contents) | Yes|
|encrypted\_message|[bytes](/API_docs/types/bytes.html) | See [Generating encrypted\_message](#generating-encrypted-message) | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Bool = $MadelineProto->auth->bindTempAuthKey(perm_auth_key_id: long, nonce: long, expires_at: int, encrypted_message: 'bytes', );
```

