---
title: "messages.getScheduledHistory"
description: "Get scheduled messages"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getScheduledHistory.html
---
# Method: messages.getScheduledHistory
[Back to methods index](index.md)



Get scheduled messages

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Peer | Optional|
|hash|[long](../types/long.md) |  | Yes|


### Return type: [messages.Messages](../types/messages.Messages.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Messages = $MadelineProto->messages->getScheduledHistory(['peer' => InputPeer, 'hash' => long, ]);
```

Or, if you're into Lua:

```lua
messages_Messages = messages.getScheduledHistory({peer=InputPeer, hash=long, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|PEER_ID_INVALID|The provided peer id is invalid|


