# messages.getInlineGameHighScores

> Get highscores of a game sent using an inline bot

[Back to methods index](index.html)



Get highscores of a game sent using an inline bot

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[InputBotInlineMessageID](/API_docs/types/InputBotInlineMessageID.html) | ID of inline message | Yes|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Get high scores of a certain user | Optional|


### Return type: [messages.HighScores](/API_docs/types/messages.HighScores.html)

### Can users use this method: **NO**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_HighScores = $MadelineProto->messages->getInlineGameHighScores(id: $InputBotInlineMessageID, user_id: $InputUser, );
```
