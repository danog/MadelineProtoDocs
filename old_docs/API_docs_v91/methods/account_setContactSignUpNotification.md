---
title: account.setContactSignUpNotification
description: Set contact sign up notification
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.setContactSignUpNotification  
[Back to methods index](index.md)


Set contact sign up notification

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|silent|[Bool](../types/Bool.md) | Silent? | Yes|


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

$Bool = $MadelineProto->account->setContactSignUpNotification(['silent' => Bool, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - account.setContactSignUpNotification
* params - `{"silent": Bool, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/account.setContactSignUpNotification`

Parameters:

silent - Json encoded Bool




Or, if you're into Lua:

```lua
Bool = account.setContactSignUpNotification({silent=Bool, })
```

