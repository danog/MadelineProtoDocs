# contacts.resetTopPeerRating

> Reset [rating](https://core.telegram.org/api/top-rating) of top peer

[Back to methods index](index.html)



Reset [rating](https://core.telegram.org/api/top-rating) of top peer

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|category|[TopPeerCategory](/API_docs/types/TopPeerCategory.html) | Top peer category | Yes|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer whose rating should be reset | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->contacts->resetTopPeerRating(category: $TopPeerCategory, peer: $InputPeer, );
```
