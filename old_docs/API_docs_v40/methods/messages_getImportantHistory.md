---
title: messages.getImportantHistory
description: Get important message history
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getImportantHistory  
[Back to methods index](index.md)


Get important message history

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Peer | Optional|
|max\_id|[int](../types/int.md) | Maximum message ID to fetch | Yes|
|min\_id|[int](../types/int.md) | Minumum message ID to fetch | Yes|
|limit|[int](../types/int.md) | Number of results to fetch | Yes|


### Return type: [messages\_Messages](../types/messages_Messages.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Messages = $MadelineProto->messages->getImportantHistory(['peer' => InputPeer, 'max_id' => int, 'min_id' => int, 'limit' => int, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - messages.getImportantHistory
* params - `{"peer": InputPeer, "max_id": int, "min_id": int, "limit": int, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.getImportantHistory`

Parameters:

peer - Json encoded InputPeer

max_id - Json encoded int

min_id - Json encoded int

limit - Json encoded int




Or, if you're into Lua:

```lua
messages_Messages = messages.getImportantHistory({peer=InputPeer, max_id=int, min_id=int, limit=int, })
```

