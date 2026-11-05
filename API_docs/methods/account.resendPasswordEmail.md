# account.resendPasswordEmail

> Resend the code to verify an email to use as [2FA recovery method](https://core.telegram.org/api/srp).

[Back to methods index](index.html)



Resend the code to verify an email to use as [2FA recovery method](https://core.telegram.org/api/srp).



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

$Bool = $MadelineProto->account->resendPasswordEmail();
```
