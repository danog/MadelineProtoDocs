---
title: messages.editChatDefaultBannedRights
description: Edit the default banned rights of a [channel/supergroup/group](https://core.telegram.org/api/channel).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_editChatDefaultBannedRights.html
---
# Method: messages.editChatDefaultBannedRights  
[Back to methods index](index.md)


Edit the default banned rights of a [channel/supergroup/group](https://core.telegram.org/api/channel).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The peer | Optional|
|banned\_rights|[ChatBannedRights](../types/ChatBannedRights.md) | The new global rights | Yes|


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

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|BANNED_RIGHTS_INVALID|You provided some invalid flags in the banned rights|
|400|CHAT_NOT_MODIFIED|The pinned message wasn't modified|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|UNTIL_DATE_INVALID|Invalid until date provided|


