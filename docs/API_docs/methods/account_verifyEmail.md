---
title: account.verifyEmail
description: Verify email address
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.verifyEmail  
[Back to methods index](index.md)


Verify email address

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|email|[string](../types/string.md) | The email address | Yes|
|code|[string](../types/string.md) | The received code | Yes|


### Return type: [Bool](../types/Bool.md)

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

$Bool = $MadelineProto->account->verifyEmail(['email' => 'string', 'code' => 'string', ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - account.verifyEmail
* params - `{"email": "string", "code": "string", }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/account.verifyEmail`

Parameters:

email - Json encoded string

code - Json encoded string




Or, if you're into Lua:

```lua
Bool = account.verifyEmail({email='string', code='string', })
```

