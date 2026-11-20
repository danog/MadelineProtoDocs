# account.updateNotifySettings

> Edits notification settings from a given user/group, from all users/all groups.

[Back to methods index](index.html)



Edits notification settings from a given user/group, from all users/all groups.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[InputNotifyPeer](/API_docs/types/InputNotifyPeer.html) | Notification source | Yes|
|settings|[InputPeerNotifySettings](/API_docs/types/InputPeerNotifySettings.html) | Notification settings | Yes|


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

$Bool = $MadelineProto->account->updateNotifySettings(peer: $InputNotifyPeer, settings: $InputPeerNotifySettings, );
```
