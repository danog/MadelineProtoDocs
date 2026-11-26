# stories.canSendStory

> Check whether we can post stories as the specified peer.

[Back to methods index](index.html)



Check whether we can post stories as the specified peer.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The peer from which we wish to post stories. | Optional|


### Return type: [stories.CanSendStoryCount](/API_docs/types/stories.CanSendStoryCount.html)

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

$stories_CanSendStoryCount = $MadelineProto->stories->canSendStory(peer: $InputPeer, );
```
