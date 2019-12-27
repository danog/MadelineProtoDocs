---
title: messages.deleteHistory
description: Deletes communication history.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.deleteHistory  
[Back to methods index](index.md)


Deletes communication history.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|just\_clear|[Bool](../types/Bool.md) | Just clear history for the current user, without actually removing messages for every chat user | Optional|
|revoke|[Bool](../types/Bool.md) | Whether to delete the message history for all chat participants | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | User or chat, communication history of which will be deleted | Optional|
|max\_id|[int](../types/int.md) | Maximum ID of message to delete | Yes|


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

$messages_AffectedHistory = $MadelineProto->messages->deleteHistory(['just_clear' => Bool, 'revoke' => Bool, 'peer' => InputPeer, 'max_id' => int, ]);
```

Or, if you're into Lua:

```lua
messages_AffectedHistory = messages.deleteHistory({just_clear=Bool, revoke=Bool, peer=InputPeer, max_id=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PEER_ID_INVALID|The provided peer id is invalid|


