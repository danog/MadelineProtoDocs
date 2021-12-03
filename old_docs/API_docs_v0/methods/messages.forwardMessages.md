---
title: messages.forwardMessages
description: Forwards messages by their IDs.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_forwardMessages.html
---
# Method: messages.forwardMessages
[Back to methods index](index.md)



Forwards messages by their IDs.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) |  | Optional|
|id|Array of [int](../types/int.md) | IDs of messages | Yes|


### Return type: [messages.StatedMessages](../types/messages.StatedMessages.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_StatedMessages = $MadelineProto->messages->forwardMessages(['peer' => InputPeer, 'id' => [int, int], ]);
```

Or, if you're into Lua:

```lua
messages_StatedMessages = messages.forwardMessages({peer=InputPeer, id={int}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|420|SLOWMODE_WAIT_X|Slowmode is enabled in this chat: wait X seconds before sending another message to this chat.|
|400|BROADCAST_PUBLIC_VOTERS_FORBIDDEN|You can't forward polls with public voters|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|CHAT_RESTRICTED|You can't send messages in this chat, you were restricted|
|400|GROUPED_MEDIA_INVALID|Invalid grouped media|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|
|400|INPUT_USER_DEACTIVATED|The specified user was deleted|
|400|MEDIA_EMPTY|The provided media object is invalid|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|
|400|MESSAGE_IDS_EMPTY|No message ids were provided|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|RANDOM_ID_INVALID|A provided random ID is invalid|
|400|SCHEDULE_DATE_TOO_LATE|You can't schedule a message this far in the future|
|400|SCHEDULE_TOO_MUCH|There are too many scheduled messages|
|400|SEND_AS_PEER_INVALID|You can't send messages as the specified peer|
|400|SLOWMODE_MULTI_MSGS_DISABLED|Slowmode is enabled, you cannot forward multiple messages to this group.|
|400|USER_BANNED_IN_CHANNEL|You're banned from sending messages in supergroups/channels|
|400|USER_IS_BLOCKED|You were blocked by this user|
|400|USER_IS_BOT|Bots can't send messages to other bots|
|400|YOU_BLOCKED_USER|You blocked this user|
|-3002|All workers are busy. Active_queries = X|All workers are busy. Active_queries = X|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|403|CHAT_SEND_GAME_FORBIDDEN|You can't send a game to this chat.|
|403|CHAT_SEND_GIFS_FORBIDDEN|You can't send gifs in this chat|
|403|CHAT_SEND_MEDIA_FORBIDDEN|You can't send media in this chat|
|403|CHAT_SEND_POLL_FORBIDDEN|You can't send polls in this chat|
|403|CHAT_SEND_STICKERS_FORBIDDEN|You can't send stickers in this chat.|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|
|403|USER_IS_BLOCKED|You were blocked by this user|
|-503|Timeout|Timeout while fetching data|


