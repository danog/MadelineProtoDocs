---
title: "messages.setInlineGameScore"
description: "Use this method to set the score of the specified user in a game sent as an inline message (bots only)."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_setInlineGameScore.html
---
# Method: messages.setInlineGameScore
[Back to methods index](index.md)



Use this method to set the score of the specified user in a game sent as an inline message (bots only).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|edit\_message|[Bool](../types/Bool.md) | Set this flag if the game message should be automatically edited to include the current scoreboard | Optional|
|force|[Bool](../types/Bool.md) | Set this flag if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters | Optional|
|id|[InputBotInlineMessageID](../types/InputBotInlineMessageID.md) | ID of the inline message | Yes|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | User identifier | Optional|
|score|[int](../types/int.md) | New score | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->setInlineGameScore(['edit_message' => Bool, 'force' => Bool, 'id' => InputBotInlineMessageID, 'user_id' => InputUser, 'score' => int, ]);
```

Or, if you're into Lua:

```lua
Bool = messages.setInlineGameScore({edit_message=Bool, force=Bool, id=InputBotInlineMessageID, user_id=InputUser, score=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|
|400|USER_BOT_REQUIRED|This method can only be called by a bot|


