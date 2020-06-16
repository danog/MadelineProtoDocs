---
title: messages.editChatAdmin
description: Make a user admin in a [legacy group](https://core.telegram.org/api/channel).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_editChatAdmin.html
---
# Method: messages.editChatAdmin
[Back to methods index](index.md)



Make a user admin in a [legacy group](https://core.telegram.org/api/channel).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) |  | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | The user to make admin | Optional|
|is\_admin|[Bool](../types/Bool.md) | Whether to make him admin | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->editChatAdmin(['chat_id' => InputPeer, 'user_id' => InputUser, 'is_admin' => Bool, ]);
```

Or, if you're into Lua:

```lua
Bool = messages.editChatAdmin({chat_id=InputPeer, user_id=InputUser, is_admin=Bool, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|USER_NOT_PARTICIPANT|You're not a member of this supergroup/channel|


