---
title: messages.setGameScore
description: Use this method to set the score of the specified user in a game sent as a normal message (bots only).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_setGameScore.html
---
# Method: messages.setGameScore
[Back to methods index](index.md)



Use this method to set the score of the specified user in a game sent as a normal message (bots only).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|edit\_message|[Bool](../types/Bool.md) | Set this flag if the game message should be automatically edited to include the current scoreboard | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Unique identifier of target chat | Optional|
|id|[int](../types/int.md) | Identifier of the sent message | Yes|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | User identifier | Optional|
|score|[int](../types/int.md) | New score | Yes|


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

$Updates = $MadelineProto->messages->setGameScore(['edit_message' => Bool, 'peer' => InputPeer, 'id' => int, 'user_id' => InputUser, 'score' => int, ]);
```

Or, if you're into Lua:

```lua
Updates = messages.setGameScore({edit_message=Bool, peer=InputPeer, id=int, user_id=InputUser, score=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|USER_BOT_REQUIRED|This method can only be called by a bot|


