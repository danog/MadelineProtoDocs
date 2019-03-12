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


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->editChatDefaultBannedRights(['peer' => InputPeer, 'banned_rights' => ChatBannedRights, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - messages.editChatDefaultBannedRights
* params - `{"peer": InputPeer, "banned_rights": ChatBannedRights, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.editChatDefaultBannedRights`

Parameters:

peer - Json encoded InputPeer

banned_rights - Json encoded ChatBannedRights




Or, if you're into Lua:

```lua
Updates = messages.editChatDefaultBannedRights({peer=InputPeer, banned_rights=ChatBannedRights, })
```

