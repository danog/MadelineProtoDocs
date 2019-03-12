---
title: account.sendVerifyPhoneCode
description: Send phone verification code
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.sendVerifyPhoneCode  
[Back to methods index](index.md)


Send phone verification code

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|allow\_flashcall|[Bool](../types/Bool.md) | Allow phone calls? | Optional|
|phone\_number|[string](../types/string.md) | The phone number | Yes|
|current\_number|[Bool](../types/Bool.md) | Is this the current number? | Optional|


### Return type: [auth\_SentCode](../types/auth_SentCode.md)

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

$auth_SentCode = $MadelineProto->account->sendVerifyPhoneCode(['allow_flashcall' => Bool, 'phone_number' => 'string', 'current_number' => Bool, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - account.sendVerifyPhoneCode
* params - `{"allow_flashcall": Bool, "phone_number": "string", "current_number": Bool, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/account.sendVerifyPhoneCode`

Parameters:

allow_flashcall - Json encoded Bool

phone_number - Json encoded string

current_number - Json encoded Bool




Or, if you're into Lua:

```lua
auth_SentCode = account.sendVerifyPhoneCode({allow_flashcall=Bool, phone_number='string', current_number=Bool, })
```

