# account.confirmPhone

> Confirm a phone number to cancel account deletion, for more info [click here »](https://core.telegram.org/api/account-deletion)

[Back to methods index](index.html)



Confirm a phone number to cancel account deletion, for more info [click here »](https://core.telegram.org/api/account-deletion)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_code\_hash|[string](/API_docs/types/string.html) | Phone code hash, for more info [click here »](https://core.telegram.org/api/account-deletion) | Optional|
|phone\_code|[string](/API_docs/types/string.html) | SMS code, for more info [click here »](https://core.telegram.org/api/account-deletion) | Optional|


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

$Bool = $MadelineProto->account->confirmPhone(phone_code_hash: 'string', phone_code: 'string', );
```
