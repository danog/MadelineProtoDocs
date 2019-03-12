---
title: account.saveSecureValue
description: Save telegram passport secure value
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.saveSecureValue  
[Back to methods index](index.md)


Save telegram passport secure value

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|value|[InputSecureValue](../types/InputSecureValue.md) | Encrypted value | Yes|
|secure\_secret\_id|[long](../types/long.md) | Secret | Yes|


### Return type: [SecureValue](../types/SecureValue.md)

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

$SecureValue = $MadelineProto->account->saveSecureValue(['value' => InputSecureValue, 'secure_secret_id' => long, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - account.saveSecureValue
* params - `{"value": InputSecureValue, "secure_secret_id": long, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/account.saveSecureValue`

Parameters:

value - Json encoded InputSecureValue

secure_secret_id - Json encoded long




Or, if you're into Lua:

```lua
SecureValue = account.saveSecureValue({value=InputSecureValue, secure_secret_id=long, })
```

