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

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->setContactSignUpNotification(['silent' => Bool, ]);
```

Or, if you're into Lua:

```lua
Bool = account.setContactSignUpNotification({silent=Bool, })
```

