---
title: messages.getMessageEditData
description: Check if about to edit a message or a media caption
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getMessageEditData  
[Back to methods index](index.md)


Check if about to edit a message or a media caption

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The chat | Optional|
|id|[int](../types/int.md) | The message ID | Yes|


### Return type: [messages\_MessageEditData](../types/messages_MessageEditData.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_MessageEditData = $MadelineProto->messages->getMessageEditData(['peer' => InputPeer, 'id' => int, ]);
```

Or, if you're into Lua:

```lua
messages_MessageEditData = messages.getMessageEditData({peer=InputPeer, id=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|403|MESSAGE_AUTHOR_REQUIRED|Message author required|


