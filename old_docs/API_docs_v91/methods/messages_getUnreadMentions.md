---
title: messages.getUnreadMentions
description: Get unread mentions
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getUnreadMentions  
[Back to methods index](index.md)


Get unread mentions

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The chat where to get unread mentions | Optional|
|offset\_id|[int](../types/int.md) | The offset | Yes|
|add\_offset|[int](../types/int.md) | The additional offset | Yes|
|limit|[int](../types/int.md) | The number of results to fetch | Yes|
|max\_id|[int](../types/int.md) | The maximum message ID to fetch | Yes|
|min\_id|[int](../types/int.md) | The minumum message ID to fetch | Yes|


### Return type: [messages\_Messages](../types/messages_Messages.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Messages = $MadelineProto->messages->getUnreadMentions(['peer' => InputPeer, 'offset_id' => int, 'add_offset' => int, 'limit' => int, 'max_id' => int, 'min_id' => int, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.getUnreadMentions`

Parameters:

peer - Json encoded InputPeer

offset_id - Json encoded int

add_offset - Json encoded int

limit - Json encoded int

max_id - Json encoded int

min_id - Json encoded int




Or, if you're into Lua:

```lua
messages_Messages = messages.getUnreadMentions({peer=InputPeer, offset_id=int, add_offset=int, limit=int, max_id=int, min_id=int, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|PEER_ID_INVALID|The provided peer id is invalid|


