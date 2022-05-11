---
title: "messages.setInlineGameScore"
description: "Use this method to set the score of the specified user in a game sent as an inline message (bots only)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_setInlineGameScore.html
---
# Method: messages.setInlineGameScore
[Back to methods index](index.html)



Use this method to set the score of the specified user in a game sent as an inline message (bots only).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|edit\_message|[Bool](/API_docs/types/Bool.html) | Set this flag if the game message should be automatically edited to include the current scoreboard | Optional|
|force|[Bool](/API_docs/types/Bool.html) | Set this flag if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters | Optional|
|id|[InputBotInlineMessageID](/API_docs/types/InputBotInlineMessageID.html) | ID of the inline message | Yes|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | User identifier | Optional|
|score|[int](/API_docs/types/int.html) | New score | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Bool = $MadelineProto->messages->setInlineGameScore(edit_message: Bool, force: Bool, id: InputBotInlineMessageID, user_id: InputUser, score: int, );
```

