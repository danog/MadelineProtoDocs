# payments.checkGiftCode

> Obtain information about a [Telegram Premium giftcode »](https://core.telegram.org/api/giveaways)

[Back to methods index](index.html)



Obtain information about a [Telegram Premium giftcode »](https://core.telegram.org/api/giveaways)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|slug|[string](/API_docs/types/string.html) | The giftcode to check | Optional|


### Return type: [payments.CheckedGiftCode](/API_docs/types/payments.CheckedGiftCode.html)

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

$payments_CheckedGiftCode = $MadelineProto->payments->checkGiftCode(slug: 'string', );
```
