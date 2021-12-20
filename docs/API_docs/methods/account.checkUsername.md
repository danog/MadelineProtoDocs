---
title: "account.checkUsername"
description: "Validates a username and checks availability."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_checkUsername.html
---
# Method: account.checkUsername
[Back to methods index](index.md)



Validates a username and checks availability.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|username|[string](../types/string.md) | username<br>Accepted characters: A-z (case-insensitive), 0-9 and underscores.<br>Length: 5-32 characters. | Yes|


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

$Bool = $MadelineProto->account->checkUsername(['username' => 'string', ]);
```

Or, if you're into Lua:

```lua
Bool = account.checkUsername({username='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|USERNAME_INVALID|The provided username is not valid|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|


