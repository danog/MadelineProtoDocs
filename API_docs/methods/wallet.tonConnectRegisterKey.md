# wallet.tonConnectRegisterKey

> wallet.tonConnectRegisterKey parameters, return type and example

[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|session\_id|[long](/API_docs/types/long.html) | Yes|
|client\_id|[string](/API_docs/types/string.html) | Optional|


### Return type: [wallet.TonConnectChallenge](/API_docs/types/wallet.TonConnectChallenge.html)

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

$wallet_TonConnectChallenge = $MadelineProto->wallet->tonConnectRegisterKey(session_id: $long, client_id: 'string', );
```
