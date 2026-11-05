# phone.getGroupCallJoinAs

> Get a list of peers that can be used to join a group call, presenting yourself as a specific user/channel.

[Back to methods index](index.html)



Get a list of peers that can be used to join a group call, presenting yourself as a specific user/channel.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The dialog whose group call or livestream we're trying to join | Optional|


### Return type: [phone.JoinAsPeers](/API_docs/types/phone.JoinAsPeers.html)

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

$phone_JoinAsPeers = $MadelineProto->phone->getGroupCallJoinAs(peer: $InputPeer, );
```
