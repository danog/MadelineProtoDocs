# stories.sendReaction

> React to a story.

[Back to methods index](index.html)



React to a story.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|add\_to\_recent|[Bool](/API_docs/types/Bool.html) | Whether to add this reaction to the [recent reactions list »](https://core.telegram.org/api/reactions#recent-reactions). | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The peer that sent the story | Optional|
|story\_id|[int](/API_docs/types/int.html) | ID of the story to react to | Optional|
|reaction|[Reaction](/API_docs/types/Reaction.html) | Reaction | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->stories->sendReaction(add_to_recent: $Bool, peer: $InputPeer, story_id: $int, reaction: $Reaction, );
```
