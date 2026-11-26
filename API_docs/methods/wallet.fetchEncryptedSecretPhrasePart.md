# wallet.fetchEncryptedSecretPhrasePart

> wallet.fetchEncryptedSecretPhrasePart parameters, return type and example

[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|token|[string](/API_docs/types/string.html) | Optional|
|public\_key|[bytes](/API_docs/types/bytes.html) | Yes|


### Return type: [wallet.EncryptedSecretPhrasePart](/API_docs/types/wallet.EncryptedSecretPhrasePart.html)

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

$wallet_EncryptedSecretPhrasePart = $MadelineProto->wallet->fetchEncryptedSecretPhrasePart(token: 'string', public_key: 'bytes', );
```
