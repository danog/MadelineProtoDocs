# account.getPrivacy

> Get privacy settings of current account

[Back to methods index](index.html)



Get privacy settings of current account

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|key|[InputPrivacyKey](/API_docs/types/InputPrivacyKey.html) | Peer category whose privacy settings should be fetched | Yes|


### Return type: [account.PrivacyRules](/API_docs/types/account.PrivacyRules.html)

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

$account_PrivacyRules = $MadelineProto->account->getPrivacy(key: $InputPrivacyKey, );
```
