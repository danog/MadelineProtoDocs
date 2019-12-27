---
title: help.getUserInfo
description: Internal use
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: help.getUserInfo  
[Back to methods index](index.md)


Internal use

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | User ID | Optional|


### Return type: [help.UserInfo](../types/help.UserInfo.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help.UserInfo = $MadelineProto->help->getUserInfo(['user_id' => InputUser, ]);
```

Or, if you're into Lua:

```lua
help.UserInfo = help.getUserInfo({user_id=InputUser, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|403|USER_INVALID|Invalid user provided|


