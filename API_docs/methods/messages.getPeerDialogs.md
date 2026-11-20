# messages.getPeerDialogs

> Get dialog info of specified peers

[Back to methods index](index.html)



Get dialog info of specified peers

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peers|Array of [InputDialogPeer](/API_docs/types/InputDialogPeer.html) | Peers | Yes|


### Return type: [messages.PeerDialogs](/API_docs/types/messages.PeerDialogs.html)

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

$messages_PeerDialogs = $MadelineProto->messages->getPeerDialogs(peers: [$InputDialogPeer, $InputDialogPeer], );
```
