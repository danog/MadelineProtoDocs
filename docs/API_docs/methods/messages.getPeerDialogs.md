---
title: "messages.getPeerDialogs"
description: "Get dialog info of specified peers"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getPeerDialogs.html
---
# Method: messages.getPeerDialogs
[Back to methods index](index.md)



Get dialog info of specified peers

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peers|Array of [Username, chat ID, Update, Message or InputDialogPeer](../types/InputDialogPeer.md) | Peers | Yes|


### Return type: [messages.PeerDialogs](../types/messages.PeerDialogs.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_PeerDialogs = $MadelineProto->messages->getPeerDialogs(['peers' => [InputDialogPeer, InputDialogPeer], ]);
```

Or, if you're into Lua:

```lua
messages_PeerDialogs = messages.getPeerDialogs({peers={InputDialogPeer}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CONNECTION_DEVICE_MODEL_EMPTY|Device model empty|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|-503|Timeout|Timeout while fetching data|


