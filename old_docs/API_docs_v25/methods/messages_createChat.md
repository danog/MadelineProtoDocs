---
title: messages.createChat
description: Create a chat (not supergroup)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.createChat  
[Back to methods index](index.md)


Create a chat (not supergroup)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|users|Array of [Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | The users to add to the chat | Yes|
|title|[string](../types/string.md) | The new chat's title | Yes|


### Return type: [messages\_StatedMessage](../types/messages_StatedMessage.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_StatedMessage = $MadelineProto->messages->createChat(['users' => [InputUser, InputUser], 'title' => 'string', ]);
```

Or, if you're into Lua:

```lua
messages_StatedMessage = messages.createChat({users={InputUser}, title='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|INPUT_USER_DEACTIVATED|The specified user was deleted|
|400|USERS_TOO_FEW|Not enough users (to create a chat, for example)|
|403|USER_RESTRICTED|You're spamreported, you can't create channels or chats.|


