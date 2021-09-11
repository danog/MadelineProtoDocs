---
title: users.getFullUser
description: Returns extended user info by ID.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/users_getFullUser.html
---
# Method: users.getFullUser
[Back to methods index](index.md)



Returns extended user info by ID.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | User ID | Optional|


### Return type: [UserFull](../types/UserFull.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$UserFull = $MadelineProto->users->getFullUser(['id' => InputUser, ]);
```

Or, if you're into Lua:

```lua
UserFull = users.getFullUser({id=InputUser, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|USER_ID_INVALID|The provided user ID is invalid|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|-500|No workers running|Internal error|
|-503|Timeout|Timeout while fetching data|


