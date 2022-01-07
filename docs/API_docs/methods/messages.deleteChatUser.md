---
title: "messages.deleteChatUser"
description: "Deletes a user from a chat and sends a service message on it."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_deleteChatUser.html
---
# Method: messages.deleteChatUser
[Back to methods index](index.html)



Deletes a user from a chat and sends a service message on it.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|revoke\_history|[Bool](/API_docs/types/Bool.html) |  | Optional|
|chat\_id|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) |  | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | User ID to be deleted | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->deleteChatUser(['revoke_history' => Bool, 'chat_id' => InputPeer, 'user_id' => InputUser, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|USER_ID_INVALID|The provided user ID is invalid|
|400|USER_NOT_PARTICIPANT|You're not a member of this supergroup/channel|


