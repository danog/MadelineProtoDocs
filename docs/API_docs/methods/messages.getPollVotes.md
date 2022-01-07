---
title: "messages.getPollVotes"
description: "Get poll results for non-anonymous polls"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getPollVotes.html
---
# Method: messages.getPollVotes
[Back to methods index](index.md)



Get poll results for non-anonymous polls

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.md) | Chat where the poll was sent | Optional|
|id|[int](/API_docs/types/int.md) | Message ID | Yes|
|option|[bytes](/API_docs/types/bytes.md) | Get only results for the specified poll `option` | Optional|
|offset|[string](/API_docs/types/string.md) | Offset for results, taken from the `next_offset` field of [messages.votesList](../constructors/messages.votesList.md), initially an empty string. <br>Note: if no more results are available, the method call will return an empty `next_offset`; thus, avoid providing the `next_offset` returned in [messages.votesList](../constructors/messages.votesList.md) if it is empty, to avoid an infinite loop. | Optional|
|limit|[int](/API_docs/types/int.md) | Number of results to return | Yes|


### Return type: [messages.VotesList](/API_docs/types/messages.VotesList.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_VotesList = $MadelineProto->messages->getPollVotes(['peer' => InputPeer, 'id' => int, 'option' => 'bytes', 'offset' => 'string', 'limit' => int, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|MSG_ID_INVALID|Invalid message ID provided|
|403|BROADCAST_FORBIDDEN|Participants of polls in channels should stay anonymous.|
|403|POLL_VOTE_REQUIRED|Cast a vote in the poll before calling this method|


