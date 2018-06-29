---
title: messages.getPeerDialogs
description: Get dialog info of peers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getPeerDialogs  
[Back to methods index](index.md)


Get dialog info of peers

### Parameters:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peers|Array of [InputDialogPeer](../types/InputDialogPeer.md) | Yes|The peers|


### Return type: [messages\_PeerDialogs](../types/messages_PeerDialogs.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_PeerDialogs = $MadelineProto->messages->getPeerDialogs(['peers' => [InputDialogPeer, InputDialogPeer], ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.getPeerDialogs`

Parameters:

peers - Json encoded  array of InputDialogPeer




Or, if you're into Lua:

```
messages_PeerDialogs = messages.getPeerDialogs({peers={InputDialogPeer}, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|PEER_ID_INVALID|The provided peer id is invalid|


