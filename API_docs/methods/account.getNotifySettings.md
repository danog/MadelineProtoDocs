# account.getNotifySettings

> Gets current notification settings for a given user/group, from all users/all groups.

[Back to methods index](index.html)



Gets current notification settings for a given user/group, from all users/all groups.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[InputNotifyPeer](/API_docs/types/InputNotifyPeer.html) | Notification source | Yes|


### Return type: [PeerNotifySettings](/API_docs/types/PeerNotifySettings.html)

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

$PeerNotifySettings = $MadelineProto->account->getNotifySettings(peer: $InputNotifyPeer, );
```
