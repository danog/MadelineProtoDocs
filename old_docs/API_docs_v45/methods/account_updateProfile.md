---
title: account.updateProfile
description: Update profile info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.updateProfile  
[Back to methods index](index.md)


Update profile info

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|first\_name|[string](../types/string.md) | The first name | Yes|
|last\_name|[string](../types/string.md) | The last name | Yes|


### Return type: [User](../types/User.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$User = $MadelineProto->account->updateProfile(['first_name' => 'string', 'last_name' => 'string', ]);
```

Or, if you're into Lua:

```lua
User = account.updateProfile({first_name='string', last_name='string', })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|ABOUT_TOO_LONG|The provided bio is too long|
|FIRSTNAME_INVALID|The first name is invalid|


