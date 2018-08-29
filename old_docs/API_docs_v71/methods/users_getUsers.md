---
title: users.getUsers
description: Get info about users
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: users.getUsers  
[Back to methods index](index.md)


Get info about users

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|Array of [Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | The ids of the users | Yes|


### Return type: [Vector\_of\_User](../types/User.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_User = $MadelineProto->users->getUsers(['id' => [InputUser, InputUser], ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - users.getUsers
* params - `{"id": [InputUser], }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/users.getUsers`

Parameters:

id - Json encoded  array of InputUser




Or, if you're into Lua:

```
Vector_of_User = users.getUsers({id={InputUser}, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|AUTH_KEY_PERM_EMPTY|The temporary auth key must be binded to the permanent auth key to use these methods.|
|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|
|MEMBER_NO_LOCATION|An internal failure occurred while fetching user info (couldn't find location)|
|NEED_MEMBER_INVALID|The provided member is invalid|
|Timeout|A timeout occurred while fetching data from the bot|


