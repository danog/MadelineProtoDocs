---
title: messages.readHistory
description: Marks message history as read.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_readHistory.html
---
# Method: messages.readHistory
[Back to methods index](index.md)



Marks message history as read.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Target user or group | Optional|
|max\_id|[int](../types/int.md) | If a positive value is passed, only messages with identifiers less or equal than the given one will be read | Yes|
|offset|[int](../types/int.md) |  | Yes|


### Return type: [messages.AffectedHistory](../types/messages.AffectedHistory.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_AffectedHistory = $MadelineProto->messages->readHistory(['peer' => InputPeer, 'max_id' => int, 'offset' => int, ]);
```

Or, if you're into Lua:

```lua
messages_AffectedHistory = messages.readHistory({peer=InputPeer, max_id=int, offset=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|-500|No workers running|Internal error|
|-503|Timeout|Timeout while fetching data|


