---
title: messages.getDiscussionMessage
description: Get [discussion message](https://core.telegram.org/api/threads) from the [associated discussion group](https://core.telegram.org/api/discussion) of a channel to show it on top of the comment section, without actually joining the group
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getDiscussionMessage.html
---
# Method: messages.getDiscussionMessage
[Back to methods index](index.md)



Get [discussion message](https://core.telegram.org/api/threads) from the [associated discussion group](https://core.telegram.org/api/discussion) of a channel to show it on top of the comment section, without actually joining the group

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | [Channel ID](https://core.telegram.org/api/channel) | Optional|
|msg\_id|[int](../types/int.md) | Message ID | Yes|


### Return type: [messages.DiscussionMessage](../types/messages.DiscussionMessage.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_DiscussionMessage = $MadelineProto->messages->getDiscussionMessage(['peer' => InputPeer, 'msg_id' => int, ]);
```

Or, if you're into Lua:

```lua
messages_DiscussionMessage = messages.getDiscussionMessage({peer=InputPeer, msg_id=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|PEER_ID_INVALID|The provided peer id is invalid|


