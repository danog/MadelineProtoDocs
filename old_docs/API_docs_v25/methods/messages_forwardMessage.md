---
title: messages.forwardMessage
description: Forward message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.forwardMessage  
[Back to methods index](index.md)


Forward message

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | From where to forward the message | Optional|
|id|[int](../types/int.md) | The message ID | Yes|


### Return type: [messages\_StatedMessage](../types/messages_StatedMessage.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_StatedMessage = $MadelineProto->messages->forwardMessage(['peer' => InputPeer, 'id' => int, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - messages.forwardMessage
* params - `{"peer": InputPeer, "id": int, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.forwardMessage`

Parameters:

peer - Json encoded InputPeer

id - Json encoded int




Or, if you're into Lua:

```lua
messages_StatedMessage = messages.forwardMessage({peer=InputPeer, id=int, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CHAT_ID_INVALID|The provided chat id is invalid|
|MESSAGE_ID_INVALID|The provided message id is invalid|
|PEER_ID_INVALID|The provided peer id is invalid|
|YOU_BLOCKED_USER|You blocked this user|


