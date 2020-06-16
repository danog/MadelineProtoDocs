---
title: messages.getCommonChats
description: Get chats in common with a user
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getCommonChats.html
---
# Method: messages.getCommonChats
[Back to methods index](index.md)



Get chats in common with a user

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | User ID | Optional|
|max\_id|[int](../types/int.md) | Maximum ID of chat to return (see [pagination](https://core.telegram.org/api/offsets)) | Yes|
|limit|[int](../types/int.md) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Yes|


### Return type: [messages.Chats](../types/messages.Chats.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.Chats = $MadelineProto->messages->getCommonChats(['user_id' => InputUser, 'max_id' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
messages.Chats = messages.getCommonChats({user_id=InputUser, max_id=int, limit=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|USER_ID_INVALID|The provided user ID is invalid|


