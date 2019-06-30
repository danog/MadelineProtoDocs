---
title: messages.readHistory
description: Mark messages as read
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.readHistory  
[Back to methods index](index.md)


Mark messages as read

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Where to mark messages as read | Optional|
|max\_id|[int](../types/int.md) | Maximum message ID to mark as read | Yes|
|offset|[int](../types/int.md) | Offset | Yes|
|read\_contents|[Bool](../types/Bool.md) | Mark messages as read? | Yes|


### Return type: [messages\_AffectedHistory](../types/messages_AffectedHistory.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_AffectedHistory = $MadelineProto->messages->readHistory(['peer' => InputPeer, 'max_id' => int, 'offset' => int, 'read_contents' => Bool, ]);
```

Or, if you're into Lua:

```lua
messages_AffectedHistory = messages.readHistory({peer=InputPeer, max_id=int, offset=int, read_contents=Bool, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|PEER_ID_INVALID|The provided peer id is invalid|
|Timeout|Timeout while fetching data|


