# payments.getStarGifts

> Get a list of available [gifts, see here »](https://core.telegram.org/api/gifts) for more info.

[Back to methods index](index.html)



Get a list of available [gifts, see here »](https://core.telegram.org/api/gifts) for more info.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) |  | Optional|


### Return type: [payments.StarGifts](/API_docs/types/payments.StarGifts.html)

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

$payments_StarGifts = $MadelineProto->payments->getStarGifts(hash: [$long\|string, $long\|string], );
```
