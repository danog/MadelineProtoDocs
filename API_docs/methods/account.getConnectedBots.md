# account.getConnectedBots

> List all currently connected [business bots »](https://core.telegram.org/api/bots/connected-business-bots)

[Back to methods index](index.html)



List all currently connected [business bots »](https://core.telegram.org/api/bots/connected-business-bots)



### Return type: [account.ConnectedBots](/API_docs/types/account.ConnectedBots.html)

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

$account_ConnectedBots = $MadelineProto->account->getConnectedBots();
```
