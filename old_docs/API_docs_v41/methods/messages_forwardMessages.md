---
title: messages.forwardMessages
description: Forward messages
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.forwardMessages  
[Back to methods index](index.md)


Forward messages

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|broadcast|[Bool](../types/Bool.md) | Broadcast this message | Optional|
|from\_peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | From where to forward the messages | Optional|
|id|Array of [int](../types/int.md) | The message IDs | Yes|
|to\_peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Where to forward the messages | Optional|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->forwardMessages(['broadcast' => Bool, 'from_peer' => InputPeer, 'id' => [int, int], 'to_peer' => InputPeer, ]);
```

Or, if you're into Lua:

```lua
Updates = messages.forwardMessages({broadcast=Bool, from_peer=InputPeer, id={int}, to_peer=InputPeer, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|GROUPED_MEDIA_INVALID|Invalid grouped media|
|400|INPUT_USER_DEACTIVATED|The specified user was deleted|
|400|MEDIA_EMPTY|The provided media object is invalid|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|
|400|MESSAGE_IDS_EMPTY|No message ids were provided|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|RANDOM_ID_INVALID|A provided random ID is invalid|
|400|USER_BANNED_IN_CHANNEL|You're banned from sending messages in supergroups/channels|
|400|USER_IS_BLOCKED|You were blocked by this user|
|400|USER_IS_BOT|Bots can't send messages to other bots|
|400|YOU_BLOCKED_USER|You blocked this user|
|403|CHAT_SEND_GIFS_FORBIDDEN|You can't send gifs in this chat|
|403|CHAT_SEND_MEDIA_FORBIDDEN|You can't send media in this chat|
|403|CHAT_SEND_STICKERS_FORBIDDEN|You can't send stickers in this chat.|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|
|-503|Timeout|Timeout while fetching data|


