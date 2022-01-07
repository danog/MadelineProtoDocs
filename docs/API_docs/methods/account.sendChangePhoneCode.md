---
title: "account.sendChangePhoneCode"
description: "Verify a new phone number to associate to the current account"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_sendChangePhoneCode.html
---
# Method: account.sendChangePhoneCode
[Back to methods index](index.html)



Verify a new phone number to associate to the current account

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_number|[string](/API_docs/types/string.html) | New phone number | Yes|
|settings|[CodeSettings](/API_docs/types/CodeSettings.html) | Phone code settings | Yes|


### Return type: [auth.SentCode](/API_docs/types/auth.SentCode.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth_SentCode = $MadelineProto->account->sendChangePhoneCode(['phone_number' => 'string', 'settings' => CodeSettings, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PHONE_NUMBER_BANNED|The provided phone number is banned from telegram|
|400|PHONE_NUMBER_INVALID|The phone number is invalid|
|400|PHONE_NUMBER_OCCUPIED|The phone number is already in use|
|406|FRESH_CHANGE_PHONE_FORBIDDEN|You can't change phone number right after logging in, please wait at least 24 hours.|
|406|PHONE_NUMBER_INVALID|The phone number is invalid|


