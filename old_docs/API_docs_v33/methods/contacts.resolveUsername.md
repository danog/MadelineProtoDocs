---
title: contacts.resolveUsername
description: Resolve a @username to get peer info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: contacts.resolveUsername  
[Back to methods index](index.md)


Resolve a @username to get peer info

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|username|[string](../types/string.md) | @username to resolve | Yes|


### Return type: [User](../types/User.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$User = $MadelineProto->contacts->resolveUsername(['username' => 'string', ]);
```

Or, if you're into Lua:

```lua
User = contacts.resolveUsername({username='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|USERNAME_INVALID|The provided username is not valid|
|400|USERNAME_NOT_OCCUPIED|The provided username is not occupied|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|401|AUTH_KEY_PERM_EMPTY|The temporary auth key must be binded to the permanent auth key to use these methods.|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|


