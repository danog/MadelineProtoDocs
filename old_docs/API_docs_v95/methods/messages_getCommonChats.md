---
title: messages.getCommonChats
description: Get chats in common with a user
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getCommonChats  
[Back to methods index](index.md)


Get chats in common with a user

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | The user | Optional|
|max\_id|[int](../types/int.md) | The maximum chat ID to fetch | Yes|
|limit|[int](../types/int.md) | Number of results to fetch | Yes|


### Return type: [messages\_Chats](../types/messages_Chats.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Chats = $MadelineProto->messages->getCommonChats(['user_id' => InputUser, 'max_id' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
messages_Chats = messages.getCommonChats({user_id=InputUser, max_id=int, limit=int, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|USER_ID_INVALID|The provided user ID is invalid|


