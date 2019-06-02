---
title: messages.setInlineGameScore
description: Set the game score of an inline message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.setInlineGameScore  
[Back to methods index](index.md)


Set the game score of an inline message

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|edit\_message|[Bool](../types/Bool.md) | Should the message with the game be edited? | Optional|
|id|[InputBotInlineMessageID](../types/InputBotInlineMessageID.md) | The ID of the inline message | Yes|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | The user that set the score | Optional|
|score|[int](../types/int.md) | The score | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->setInlineGameScore(['edit_message' => Bool, 'id' => InputBotInlineMessageID, 'user_id' => InputUser, 'score' => int, ]);
```

Or, if you're into Lua:

```lua
Bool = messages.setInlineGameScore({edit_message=Bool, id=InputBotInlineMessageID, user_id=InputUser, score=int, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|MESSAGE_ID_INVALID|The provided message id is invalid|
|USER_BOT_REQUIRED|This method can only be called by a bot|


