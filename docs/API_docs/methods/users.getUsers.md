---
title: "users.getUsers"
description: "Returns basic user info according to their identifiers."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/users_getUsers.html
---
# Method: users.getUsers
[Back to methods index](index.html)



Returns basic user info according to their identifiers.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|Array of [Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | List of user identifiers | Yes|


### Return type: [Vector\_of\_User](/API_docs/types/User.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Vector_of_User = $MadelineProto->users->getUsers(id: [InputUser, InputUser], );
```

