---
title: account.sendVerifyEmailCode
description: Send email verification code
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.sendVerifyEmailCode  
[Back to methods index](index.md)


Send email verification code

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|email|[string](../types/string.md) | Email | Yes|


### Return type: [account\_SentEmailCode](../types/account_SentEmailCode.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_SentEmailCode = $MadelineProto->account->sendVerifyEmailCode(['email' => 'string', ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - account.sendVerifyEmailCode
* params - `{"email": "string", }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/account.sendVerifyEmailCode`

Parameters:

email - Json encoded string




Or, if you're into Lua:

```lua
account_SentEmailCode = account.sendVerifyEmailCode({email='string', })
```

