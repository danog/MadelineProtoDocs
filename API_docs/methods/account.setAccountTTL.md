# account.setAccountTTL

> Set account self-destruction period

[Back to methods index](index.html)



Set account self-destruction period

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|ttl|[AccountDaysTTL](/API_docs/types/AccountDaysTTL.html) | Time to live in days | Yes|


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

$Bool = $MadelineProto->account->setAccountTTL(ttl: $AccountDaysTTL, );
```
