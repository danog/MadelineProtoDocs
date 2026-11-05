# stories.getPeerMaxIDs

> Get the IDs of the maximum read stories for a set of peers.

[Back to methods index](index.html)



Get the IDs of the maximum read stories for a set of peers.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|Array of [Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peers | Yes|


### Return type: [Vector\_of\_RecentStory](/API_docs/types/RecentStory.html)

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

$Vector_of_RecentStory = $MadelineProto->stories->getPeerMaxIDs(id: [$InputPeer, $InputPeer], );
```
