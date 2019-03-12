---
title: messages.sendVote
description: Send vote
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.sendVote  
[Back to methods index](index.md)


Send vote

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Peer | Optional|
|msg\_id|[int](../types/int.md) | Message ID | Yes|
|options|Array of [bytes](../types/bytes.md) | Options | Yes|


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

$Updates = $MadelineProto->messages->sendVote(['peer' => InputPeer, 'msg_id' => int, 'options' => ['bytes', 'bytes'], ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - messages.sendVote
* params - `{"peer": InputPeer, "msg_id": int, "options": [{"_": "bytes", "bytes":"base64 encoded bytes"}], }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.sendVote`

Parameters:

peer - Json encoded InputPeer

msg_id - Json encoded int

options - Json encoded  array of bytes




Or, if you're into Lua:

```lua
Updates = messages.sendVote({peer=InputPeer, msg_id=int, options={'bytes'}, })
```

