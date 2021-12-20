---
title: "account.setContactSignUpNotification"
description: "Toggle contact sign up notifications"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_setContactSignUpNotification.html
---
# Method: account.setContactSignUpNotification
[Back to methods index](index.md)



Toggle contact sign up notifications

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|silent|[Bool](../types/Bool.md) | Whether to disable contact sign up notifications | Yes|


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

