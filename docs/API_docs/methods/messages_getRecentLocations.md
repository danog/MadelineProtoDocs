---
title: messages.getRecentLocations
description: Get recent locations
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getRecentLocations  
[Back to methods index](index.md)


Get recent locations

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The chat where to search locations | Optional|
|limit|[int](../types/int.md) | Number of results to return | Yes|
|hash|[int](../types/int.md) | $MadelineProto->gen_vector_hash(ids of previously fetched locations, or []); | Yes|


### Return type: [messages\_Messages](../types/messages_Messages.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Messages = $MadelineProto->messages->getRecentLocations(['peer' => InputPeer, 'limit' => int, 'hash' => int, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - messages.getRecentLocations
* params - `{"peer": InputPeer, "limit": int, "hash": int, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.getRecentLocations`

Parameters:

peer - Json encoded InputPeer

limit - Json encoded int

hash - Json encoded int




Or, if you're into Lua:

```
messages_Messages = messages.getRecentLocations({peer=InputPeer, limit=int, hash=int, })
```

