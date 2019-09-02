---
title: messages.deleteChatUser
description: Delete a user from a chat (not supergroup)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.deleteChatUser  
[Back to methods index](index.md)


Delete a user from a chat (not supergroup)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The ID of the chat | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | The user to delete (pass @me to leave the chat) | Optional|


### Return type: [messages\_StatedMessage](../types/messages_StatedMessage.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_StatedMessage = $MadelineProto->messages->deleteChatUser(['chat_id' => InputPeer, 'user_id' => InputUser, ]);
```

Or, if you're into Lua:

```lua
messages_StatedMessage = messages.deleteChatUser({chat_id=InputPeer, user_id=InputUser, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|USER_NOT_PARTICIPANT|You're not a member of this supergroup/channel|


