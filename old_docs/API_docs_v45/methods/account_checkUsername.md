---
title: account.checkUsername
description: Check if this username is available
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.checkUsername  
[Back to methods index](index.md)


Check if this username is available

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|username|[string](../types/string.md) | The username to check | Yes|


### Return type: [Bool](../types/Bool.md)

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

$Bool = $MadelineProto->account->checkUsername(['username' => 'string', ]);
```

Or, if you're into Lua:

```lua
Bool = account.checkUsername({username='string', })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|USERNAME_INVALID|The provided username is not valid|


