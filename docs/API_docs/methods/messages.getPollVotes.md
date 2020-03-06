---
title: messages.getPollVotes
description: messages.getPollVotes parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getPollVotes.html
---
# Method: messages.getPollVotes  
[Back to methods index](index.md)


### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|
|id|[int](../types/int.md) | Yes|
|option|[bytes](../types/bytes.md) | Optional|
|offset|[string](../types/string.md) | Optional|
|limit|[int](../types/int.md) | Yes|


### Return type: [messages.VotesList](../types/messages.VotesList.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.VotesList = $MadelineProto->messages->getPollVotes(['peer' => InputPeer, 'id' => int, 'option' => 'bytes', 'offset' => 'string', 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
messages.VotesList = messages.getPollVotes({peer=InputPeer, id=int, option='bytes', offset='string', limit=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|403|POLL_VOTE_REQUIRED|Cast a vote in the poll before calling this method|


