---
title: messages.getMessageEditData
description: Check if about to edit a message or a media caption
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getMessageEditData  
[Back to methods index](index.md)


Check if about to edit a message or a media caption

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The chat | Optional|
|id|[int](../types/int.md) | The message ID | Yes|


### Return type: [messages\_MessageEditData](../types/messages_MessageEditData.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_MessageEditData = $MadelineProto->messages->getMessageEditData(['peer' => InputPeer, 'id' => int, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.getMessageEditData`

Parameters:

peer - Json encoded InputPeer

id - Json encoded int




Or, if you're into Lua:

```
messages_MessageEditData = messages.getMessageEditData({peer=InputPeer, id=int, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|PEER_ID_INVALID|The provided peer id is invalid|
|MESSAGE_AUTHOR_REQUIRED|Message author required|


