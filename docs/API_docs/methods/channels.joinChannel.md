---
title: "channels.joinChannel"
description: "Join a channel/supergroup"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_joinChannel.html
---
# Method: channels.joinChannel
[Back to methods index](index.md)



Join a channel/supergroup

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.md) | Channel/supergroup to join | Optional|


### Return type: [Updates](/API_docs/types/Updates.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->channels->joinChannel(['channel' => InputChannel, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHANNELS_TOO_MUCH|You have joined too many channels/supergroups|
|400|CHAT_INVALID|Invalid chat|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|
|400|INVITE_HASH_EMPTY|The invite hash is empty|
|400|INVITE_HASH_EXPIRED|The invite link has expired|
|400|INVITE_HASH_INVALID|The invite hash is invalid|
|400|INVITE_REQUEST_SENT||
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|USER_ALREADY_PARTICIPANT|The user is already in the group|
|400|USER_CHANNELS_TOO_MUCH|One of the users you tried to add is already in too many channels/supergroups|
|400|USERS_TOO_MUCH|The maximum number of users has been exceeded (to create a chat, for example)|
|-3002|All workers are busy. Active_queries = X|All workers are busy. Active_queries = X|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|406|INVITE_HASH_EXPIRED|The invite link has expired|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|
|-503|Timeout|Timeout while fetching data|


