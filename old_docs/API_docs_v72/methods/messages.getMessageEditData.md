---
title: messages.getMessageEditData
description: Find out if a media message's caption can be edited
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getMessageEditData  
[Back to methods index](index.md)


Find out if a media message's caption can be edited

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Peer where the media was sent | Optional|
|id|[int](../types/int.md) | ID of message | Yes|


### Return type: [messages.MessageEditData](../types/messages.MessageEditData.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.MessageEditData = $MadelineProto->messages->getMessageEditData(['peer' => InputPeer, 'id' => int, ]);
```

Or, if you're into Lua:

```lua
messages.MessageEditData = messages.getMessageEditData({peer=InputPeer, id=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|403|MESSAGE_AUTHOR_REQUIRED|Message author required|


