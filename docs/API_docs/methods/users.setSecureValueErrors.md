---
title: "users.setSecureValueErrors"
description: "Notify the user that the sent [passport](https://core.telegram.org/passport) data contains some errors The user will not be able to re-submit their Passport data to you until the errors are fixed (the contents of the field for which you returned the error must change)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/users_setSecureValueErrors.html
---
# Method: users.setSecureValueErrors
[Back to methods index](index.md)



Notify the user that the sent [passport](https://core.telegram.org/passport) data contains some errors The user will not be able to re-submit their Passport data to you until the errors are fixed (the contents of the field for which you returned the error must change).

Use this if the data submitted by the user doesn't satisfy the standards your service requires for any reason. For example, if a birthday date seems invalid, a submitted document is blurry, a scan shows evidence of tampering, etc. Supply some details in the error message to make sure the user knows how to correct the issues.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | The user | Optional|
|errors|Array of [SecureValueError](../types/SecureValueError.md) | Errors | Yes|


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

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|USER_ID_INVALID|The provided user ID is invalid|


