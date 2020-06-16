---
title: messages.forwardMessage
description: messages.forwardMessage parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_forwardMessage.html
---
# Method: messages.forwardMessage
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|
|id|[int](../types/int.md) | Yes|


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

$Updates = $MadelineProto->messages->forwardMessage(['peer' => InputPeer, 'id' => int, ]);
```

Or, if you're into Lua:

```lua
Updates = messages.forwardMessage({peer=InputPeer, id=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|YOU_BLOCKED_USER|You blocked this user|


