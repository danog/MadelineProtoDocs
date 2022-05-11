---
title: "messages.getGameHighScores"
description: "Get highscores of a game"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getGameHighScores.html
---
# Method: messages.getGameHighScores
[Back to methods index](index.html)



Get highscores of a game

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Where was the game sent | Optional|
|id|[int](/API_docs/types/int.html) | ID of message with game media attachment | Yes|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Get high scores made by a certain user | Optional|


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
$messages_HighScores = $MadelineProto->messages->getGameHighScores(peer: InputPeer, id: int, user_id: InputUser, );
```

