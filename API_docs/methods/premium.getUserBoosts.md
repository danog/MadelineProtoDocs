# premium.getUserBoosts

> Returns the lists of boost that were applied to a channel/supergroup by a specific user (admins only)

[Back to methods index](index.html)



Returns the lists of boost that were applied to a channel/supergroup by a specific user (admins only)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The channel/supergroup | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The user | Optional|


### Return type: [premium.BoostsList](/API_docs/types/premium.BoostsList.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$premium_BoostsList = $MadelineProto->premium->getUserBoosts(peer: $InputPeer, user_id: $InputUser, );
```
