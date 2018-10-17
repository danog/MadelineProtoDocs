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
|device\_model|[string](../types/string.md) | Device model | Yes|
|system\_version|[string](../types/string.md) | System version | Yes|
|app\_version|[string](../types/string.md) | App version | Yes|
|app\_sandbox|[Bool](../types/Bool.md) | Should the app run in a sandbox? | Yes|
|lang\_code|[string](../types/string.md) | Language code | Yes|


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

$Bool = $MadelineProto->account->registerDevice(['token_type' => int, 'token' => 'string', 'device_model' => 'string', 'system_version' => 'string', 'app_version' => 'string', 'app_sandbox' => Bool, 'lang_code' => 'string', ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/account.registerDevice`

Parameters:

token_type - Json encoded int

token - Json encoded string

device_model - Json encoded string

system_version - Json encoded string

app_version - Json encoded string

app_sandbox - Json encoded Bool

lang_code - Json encoded string




Or, if you're into Lua:

```lua
Bool = account.registerDevice({token_type=int, token='string', device_model='string', system_version='string', app_version='string', app_sandbox=Bool, lang_code='string', })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|TOKEN_INVALID|The provided token is invalid|


