---
title: messages.updatePinnedMessage
description: Update pinned message (private chat only)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.updatePinnedMessage  
[Back to methods index](index.md)


Update pinned message (private chat only)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|silent|[Bool](../types/Bool.md) | Silent? | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Peer | Optional|
|id|[int](../types/int.md) | Message ID | Yes|


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

$Updates = $MadelineProto->messages->updatePinnedMessage(['silent' => Bool, 'peer' => InputPeer, 'id' => int, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - messages.updatePinnedMessage
* params - `{"silent": Bool, "peer": InputPeer, "id": int, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.updatePinnedMessage`

Parameters:

silent - Json encoded Bool

peer - Json encoded InputPeer

id - Json encoded int




Or, if you're into Lua:

```lua
Updates = messages.updatePinnedMessage({silent=Bool, peer=InputPeer, id=int, })
```

