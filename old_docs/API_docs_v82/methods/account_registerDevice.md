---
title: account.registerDevice
description: Register device for push notifications
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.registerDevice  
[Back to methods index](index.md)


Register device for push notifications

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|token\_type|[int](../types/int.md) | Device token type. Possible values: 1 - APNS, 2 - GCM, 3 - MPNS, 4 - Simple Push, 5 - Ubuntu Phone, 6 - Blackberry, and other, see source code of official apps for more info | Yes|
|token|[string](../types/string.md) | Device token type. Possible values: 1 - APNS, 2 - GCM, 3 - MPNS, 4 - Simple Push, 5 - Ubuntu Phone,6 - Blackberry, and other, see source code of official apps for more info | Yes|
|app\_sandbox|[Bool](../types/Bool.md) | Should the app run in a sandbox? | Yes|
|secret|[bytes](../types/bytes.md) | Secret | Yes|
|other\_uids|Array of [int](../types/int.md) | Other UIDs | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->registerDevice(['token_type' => int, 'token' => 'string', 'app_sandbox' => Bool, 'secret' => 'bytes', 'other_uids' => [int, int], ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/account.registerDevice`

Parameters:

token_type - Json encoded int

token - Json encoded string

app_sandbox - Json encoded Bool

secret - Json encoded bytes

other_uids - Json encoded  array of int




Or, if you're into Lua:

```lua
Bool = account.registerDevice({token_type=int, token='string', app_sandbox=Bool, secret='bytes', other_uids={int}, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|TOKEN_INVALID|The provided token is invalid|


