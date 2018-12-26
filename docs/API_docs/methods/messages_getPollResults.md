---
title: messages.getPollResults
description: Get poll results
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getPollResults  
[Back to methods index](index.md)


Get poll results

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Peer | Optional|
|msg\_id|[int](../types/int.md) | Message ID | Yes|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->getPollResults(['peer' => InputPeer, 'msg_id' => int, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - messages.getPollResults
* params - `{"peer": InputPeer, "msg_id": int, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.getPollResults`

Parameters:

peer - Json encoded InputPeer

msg_id - Json encoded int




Or, if you're into Lua:

```lua
Updates = messages.getPollResults({peer=InputPeer, msg_id=int, })
```

