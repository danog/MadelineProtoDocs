---
title: "messages.getHistory"
description: "Gets back the conversation history with one interlocutor / within a chat"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getHistory.html
---
# Method: messages.getHistory
[Back to methods index](index.md)



Gets back the conversation history with one interlocutor / within a chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.md) | Target peer | Optional|
|offset\_id|[int](/API_docs/types/int.md) | Only return messages starting from the specified message ID | Yes|
|offset\_date|[int](/API_docs/types/int.md) | Only return messages sent before the specified date | Yes|
|add\_offset|[int](/API_docs/types/int.md) | Number of list elements to be skipped, negative values are also accepted. | Yes|
|limit|[int](/API_docs/types/int.md) | Number of results to return | Yes|
|max\_id|[int](/API_docs/types/int.md) | If a positive value was transferred, the method will return only messages with IDs less than **max\_id** | Yes|
|min\_id|[int](/API_docs/types/int.md) | If a positive value was transferred, the method will return only messages with IDs more than **min\_id** | Yes|
|hash|[long](/API_docs/types/long.md) |  | Yes|


### Return type: [messages.Messages](/API_docs/types/messages.Messages.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Messages = $MadelineProto->messages->getHistory(['peer' => InputPeer, 'offset_id' => int, 'offset_date' => int, 'add_offset' => int, 'limit' => int, 'max_id' => int, 'min_id' => int, 'hash' => long, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|CONNECTION_DEVICE_MODEL_EMPTY|Device model empty|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|-3002|All workers are busy. Active_queries = X|All workers are busy. Active_queries = X|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|401|AUTH_KEY_PERM_EMPTY|The temporary auth key must be binded to the permanent auth key to use these methods.|
|-504|memory limit exit|Internal error|
|-503|Timeout|Timeout while fetching data|


