# stories.getStoriesViews

> Obtain info about the view count, forward count, reactions and recent viewers of one or more [stories](https://core.telegram.org/api/stories).

[Back to methods index](index.html)



Obtain info about the view count, forward count, reactions and recent viewers of one or more [stories](https://core.telegram.org/api/stories).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer whose stories should be fetched | Optional|
|id|Array of [int](/API_docs/types/int.html) | Story IDs | Yes|


### Return type: [stories.StoryViews](/API_docs/types/stories.StoryViews.html)

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

$stories_StoryViews = $MadelineProto->stories->getStoriesViews(peer: $InputPeer, id: [$int, $int], );
```
