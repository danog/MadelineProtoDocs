# wallet.getExistingWaltBalance

> wallet.getExistingWaltBalance parameters, return type and example

[Back to methods index](index.html)





### Return type: [wallet.ExistingBalance](/API_docs/types/wallet.ExistingBalance.html)

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

$wallet_ExistingBalance = $MadelineProto->wallet->getExistingWaltBalance();
```
