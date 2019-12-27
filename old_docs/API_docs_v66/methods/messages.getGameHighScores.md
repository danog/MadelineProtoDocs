---
title: messages.getGameHighScores
description: Get highscores of a game
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getGameHighScores  
[Back to methods index](index.md)


Get highscores of a game

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Where was the game sent | Optional|
|id|[int](../types/int.md) | ID of message with game media attachment | Yes|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | Get high scores made by a certain user | Optional|


### Return type: [messages\_HighScores](../types/messages_HighScores.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_HighScores = $MadelineProto->messages->getGameHighScores(['peer' => InputPeer, 'id' => int, 'user_id' => InputUser, ]);
```

Or, if you're into Lua:

```lua
messages_HighScores = messages.getGameHighScores({peer=InputPeer, id=int, user_id=InputUser, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|USER_BOT_REQUIRED|This method can only be called by a bot|


