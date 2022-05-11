---
title: "messages.getInlineGameHighScores"
description: "Get highscores of a game sent using an inline bot"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getInlineGameHighScores.html
---
# Method: messages.getInlineGameHighScores
[Back to methods index](index.html)



Get highscores of a game sent using an inline bot

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[InputBotInlineMessageID](/API_docs/types/InputBotInlineMessageID.html) | ID of inline message | Yes|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Get high scores of a certain user | Optional|


### Return type: [messages.HighScores](/API_docs/types/messages.HighScores.html)

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
$messages_HighScores = $MadelineProto->messages->getInlineGameHighScores(id: InputBotInlineMessageID, user_id: InputUser, );
```

