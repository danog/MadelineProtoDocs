---
title: messages.getMessagesViews
description: Get and increase message views
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getMessagesViews  
[Back to methods index](index.md)


Get and increase message views

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The chat where the message is located | Optional|
|id|Array of [int](../types/int.md) | The IDs messages to get | Yes|
|increment|[Bool](../types/Bool.md) | Increase message views? | Yes|


### Return type: [Vector\_of\_int](../types/int.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_int = $MadelineProto->messages->getMessagesViews(['peer' => InputPeer, 'id' => [int, int], 'increment' => Bool, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.getMessagesViews`

Parameters:

peer - Json encoded InputPeer

id - Json encoded  array of int

increment - Json encoded Bool




Or, if you're into Lua:

```
Vector_of_int = messages.getMessagesViews({peer=InputPeer, id={int}, increment=Bool, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|CHAT_ID_INVALID|The provided chat id is invalid|
|PEER_ID_INVALID|The provided peer id is invalid|


