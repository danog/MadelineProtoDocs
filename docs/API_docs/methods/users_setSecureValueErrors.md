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


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->users->setSecureValueErrors(['id' => InputUser, 'errors' => [SecureValueError, SecureValueError], ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - users.setSecureValueErrors
* params - `{"id": InputUser, "errors": [SecureValueError], }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/users.setSecureValueErrors`

Parameters:

id - Json encoded InputUser

errors - Json encoded  array of SecureValueError




Or, if you're into Lua:

```
Bool = users.setSecureValueErrors({id=InputUser, errors={SecureValueError}, })
```

