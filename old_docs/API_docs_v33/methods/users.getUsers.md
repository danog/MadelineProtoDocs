---
title: users.getUsers
description: Returns basic user info according to their identifiers.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: users.getUsers  
[Back to methods index](index.md)


Returns basic user info according to their identifiers.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|Array of [Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | The ids of the users | Yes|


### Return type: [Vector\_of\_User](../types/User.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_User = $MadelineProto->users->getUsers(['id' => [InputUser, InputUser], ]);
```

Or, if you're into Lua:

```lua
Vector_of_User = users.getUsers({id={InputUser}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|MSG_ID_INVALID|Invalid message ID provided|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|401|AUTH_KEY_PERM_EMPTY|The temporary auth key must be binded to the permanent auth key to use these methods.|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|
|-503|Timeout|Timeout while fetching data|


