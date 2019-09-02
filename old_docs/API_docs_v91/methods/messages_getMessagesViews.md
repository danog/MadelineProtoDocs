---
title: messages.getMessagesViews
description: Get and increase message views
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getMessagesViews  
[Back to methods index](index.md)


Get and increase message views

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The chat where the message is located | Optional|
|id|Array of [int](../types/int.md) | The IDs messages to get | Yes|
|increment|[Bool](../types/Bool.md) | Increase message views? | Yes|


### Return type: [Vector\_of\_int](../types/int.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_int = $MadelineProto->messages->getMessagesViews(['peer' => InputPeer, 'id' => [int, int], 'increment' => Bool, ]);
```

Or, if you're into Lua:

```lua
Vector_of_int = messages.getMessagesViews({peer=InputPeer, id={int}, increment=Bool, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|PEER_ID_INVALID|The provided peer id is invalid|


