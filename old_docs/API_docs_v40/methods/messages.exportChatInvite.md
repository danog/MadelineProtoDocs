---
title: messages.exportChatInvite
description: Export an invite link for a chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_exportChatInvite.html
---
# Method: messages.exportChatInvite
[Back to methods index](index.md)



Export an invite link for a chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Chat | Optional|


### Return type: [ExportedChatInvite](../types/ExportedChatInvite.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$ExportedChatInvite = $MadelineProto->messages->exportChatInvite(['peer' => InputPeer, ]);
```

Or, if you're into Lua:

```lua
ExportedChatInvite = messages.exportChatInvite({peer=InputPeer, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|


