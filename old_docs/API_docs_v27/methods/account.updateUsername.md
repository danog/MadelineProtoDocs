---
title: account.updateUsername
description: Changes username for the current user.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_updateUsername.html
---
# Method: account.updateUsername  
[Back to methods index](index.md)


Changes username for the current user.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|username|[string](../types/string.md) | Username or empty string if username is to be removed<br>Accepted characters: a-z (case-insensitive), 0-9 and underscores.<br>Length: 5-32 characters. | Yes|


### Return type: [User](../types/User.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$User = $MadelineProto->account->updateUsername(['username' => 'string', ]);
```

Or, if you're into Lua:

```lua
User = account.updateUsername({username='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|USERNAME_INVALID|The provided username is not valid|
|400|USERNAME_NOT_MODIFIED|The username was not modified|
|400|USERNAME_OCCUPIED|The provided username is already occupied|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|


