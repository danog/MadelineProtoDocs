---
title: "messages.createChat"
description: "Creates a new chat."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_createChat.html
---
# Method: messages.createChat
[Back to methods index](index.md)



Creates a new chat.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|users|Array of [Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.md) | List of user IDs to be invited | Yes|
|title|[string](/API_docs/types/string.md) | Chat name | Yes|


### Return type: [Updates](/API_docs/types/Updates.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->createChat(['users' => [InputUser, InputUser], 'title' => 'string', ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHAT_INVALID|Invalid chat|
|400|CHAT_TITLE_EMPTY|No chat title provided|
|400|INPUT_USER_DEACTIVATED|The specified user was deleted|
|400|USERS_TOO_FEW|Not enough users (to create a chat, for example)|
|403|USER_RESTRICTED|You're spamreported, you can't create channels or chats.|


