---
title: messages.getChats
description: Returns chat basic info on their IDs.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getChats  
[Back to methods index](index.md)


Returns chat basic info on their IDs.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|Array of [int](../types/int.md) | The MTProto IDs of chats to fetch info about | Yes|


### Return type: [messages\_Chats](../types/messages_Chats.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Chats = $MadelineProto->messages->getChats(['id' => [int, int], ]);
```

Or, if you're into Lua:

```lua
messages_Chats = messages.getChats({id={int}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|PEER_ID_INVALID|The provided peer id is invalid|


