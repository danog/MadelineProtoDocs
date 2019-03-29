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


### Return type: [Updates](../types/Updates.md)

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

$Updates = $MadelineProto->messages->createChat(['users' => [InputUser, InputUser], 'title' => 'string', ]);
```

Or, if you're into Lua:

```lua
Updates = messages.createChat({users={InputUser}, title='string', })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|USERS_TOO_FEW|Not enough users (to create a chat, for example)|
|USER_RESTRICTED|You're spamreported, you can't create channels or chats.|


