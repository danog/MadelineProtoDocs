---
title: account.getContactSignUpNotification
description: Contact signup notification setting value
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.getContactSignUpNotification  
[Back to methods index](index.md)


Contact signup notification setting value



### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->getContactSignUpNotification();
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - account.getContactSignUpNotification
* params - `{}`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/account.getContactSignUpNotification`

Parameters:




Or, if you're into Lua:

```lua
Bool = account.getContactSignUpNotification({})
```

