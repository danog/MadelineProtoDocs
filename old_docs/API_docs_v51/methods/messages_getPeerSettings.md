---
title: messages.getPeerSettings
description: Get the settings of  apeer
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getPeerSettings  
[Back to methods index](index.md)


Get the settings of  apeer

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The peer | Optional|


### Return type: [PeerSettings](../types/PeerSettings.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$PeerSettings = $MadelineProto->messages->getPeerSettings(['peer' => InputPeer, ]);
```

Or, if you're into Lua:

```lua
PeerSettings = messages.getPeerSettings({peer=InputPeer, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CHANNEL_INVALID|The provided channel is invalid|
|PEER_ID_INVALID|The provided peer id is invalid|


