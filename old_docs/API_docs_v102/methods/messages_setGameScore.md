---
title: messages.setGameScore
description: Set the game score
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.setGameScore  
[Back to methods index](index.md)


Set the game score

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|edit\_message|[Bool](../types/Bool.md) | Should the message with the game be edited? | Optional|
|force|[Bool](../types/Bool.md) | Force setting the game score | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The chat where the game was sent | Optional|
|id|[int](../types/int.md) | The message ID | Yes|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | The user that set the score | Optional|
|score|[int](../types/int.md) | The score | Yes|


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

$Updates = $MadelineProto->messages->setGameScore(['edit_message' => Bool, 'force' => Bool, 'peer' => InputPeer, 'id' => int, 'user_id' => InputUser, 'score' => int, ]);
```

Or, if you're into Lua:

```lua
Updates = messages.setGameScore({edit_message=Bool, force=Bool, peer=InputPeer, id=int, user_id=InputUser, score=int, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|PEER_ID_INVALID|The provided peer id is invalid|
|USER_BOT_REQUIRED|This method can only be called by a bot|


