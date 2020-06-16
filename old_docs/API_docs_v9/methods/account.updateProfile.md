---
title: account.updateProfile
description: Updates user profile.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_updateProfile.html
---
# Method: account.updateProfile
[Back to methods index](index.md)



Updates user profile.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|first\_name|[string](../types/string.md) | New user first name | Yes|
|last\_name|[string](../types/string.md) | New user last name | Yes|


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

$User = $MadelineProto->account->updateProfile(['first_name' => 'string', 'last_name' => 'string', ]);
```

Or, if you're into Lua:

```lua
User = account.updateProfile({first_name='string', last_name='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|ABOUT_TOO_LONG|About string too long|
|400|FIRSTNAME_INVALID|The first name is invalid|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|
|-503|Timeout|Timeout while fetching data|


