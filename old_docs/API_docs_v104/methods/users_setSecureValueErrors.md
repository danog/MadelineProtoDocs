---
title: users.setSecureValueErrors
description: Set secure value error for telegram passport
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: users.setSecureValueErrors  
[Back to methods index](index.md)


Set secure value error for telegram passport

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | The user ID | Optional|
|errors|Array of [SecureValueError](../types/SecureValueError.md) | The errors | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->users->setSecureValueErrors(['id' => InputUser, 'errors' => [SecureValueError, SecureValueError], ]);
```

Or, if you're into Lua:

```lua
Bool = users.setSecureValueErrors({id=InputUser, errors={SecureValueError}, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|USER_ID_INVALID|The provided user ID is invalid|


