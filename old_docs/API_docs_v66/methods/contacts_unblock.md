---
title: contacts.unblock
description: Unblock a user
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: contacts.unblock  
[Back to methods index](index.md)


Unblock a user

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | The user to unblock | Optional|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->contacts->unblock(['id' => InputUser, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/contacts.unblock`

Parameters:

id - Json encoded InputUser




Or, if you're into Lua:

```lua
Bool = contacts.unblock({id=InputUser, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CONTACT_ID_INVALID|The provided contact ID is invalid|


