---
title: account.verifyPhone
description: Verify phone number
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.verifyPhone  
[Back to methods index](index.md)


Verify phone number

### Parameters:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_number|[string](../types/string.md) | Yes|The phone number|
|phone\_code\_hash|[string](../types/string.md) | Yes|The phone code hash returned by account.sendVerifyPhoneCode|
|phone\_code|[string](../types/string.md) | Yes|The phone code type returned by account.sendVerifyPhoneCode|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->verifyPhone(['phone_number' => 'string', 'phone_code_hash' => 'string', 'phone_code' => 'string', ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - account.verifyPhone
* params - `{"phone_number": "string", "phone_code_hash": "string", "phone_code": "string", }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/account.verifyPhone`

Parameters:

phone_number - Json encoded string

phone_code_hash - Json encoded string

phone_code - Json encoded string




Or, if you're into Lua:

```
Bool = account.verifyPhone({phone_number='string', phone_code_hash='string', phone_code='string', })
```

