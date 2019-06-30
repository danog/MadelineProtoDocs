---
title: messages.editChatDefaultBannedRights
description: Edit default rights of chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.editChatDefaultBannedRights  
[Back to methods index](index.md)


Edit default rights of chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Chat | Optional|
|banned\_rights|[ChatBannedRights](../types/ChatBannedRights.md) | Global chat rights | Yes|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->editChatDefaultBannedRights(['peer' => InputPeer, 'banned_rights' => ChatBannedRights, ]);
```

Or, if you're into Lua:

```lua
Updates = messages.editChatDefaultBannedRights({peer=InputPeer, banned_rights=ChatBannedRights, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|PEER_ID_INVALID|The provided peer id is invalid|


