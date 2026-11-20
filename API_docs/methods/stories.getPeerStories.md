# stories.getPeerStories

> Fetch the full active [story list](https://core.telegram.org/api/stories#watching-stories) of a specific peer.

[Back to methods index](index.html)



Fetch the full active [story list](https://core.telegram.org/api/stories#watching-stories) of a specific peer.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer whose stories should be fetched | Optional|


### Return type: [stories.PeerStories](/API_docs/types/stories.PeerStories.html)

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

$stories_PeerStories = $MadelineProto->stories->getPeerStories(peer: $InputPeer, );
```
