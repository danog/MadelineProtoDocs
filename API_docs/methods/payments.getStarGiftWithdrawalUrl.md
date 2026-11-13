# payments.getStarGiftWithdrawalUrl

> Convert a [collectible gift »](https://core.telegram.org/api/gifts) to an NFT on the TON blockchain.

[Back to methods index](index.html)



Convert a [collectible gift »](https://core.telegram.org/api/gifts) to an NFT on the TON blockchain.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|stargift|[InputSavedStarGift](/API_docs/types/InputSavedStarGift.html) | The collectible gift to export. | Yes|
|tmp\_password|[bytes](/API_docs/types/bytes.html) |  | Yes|


### Return type: [payments.StarGiftWithdrawalUrl](/API_docs/types/payments.StarGiftWithdrawalUrl.html)

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

$payments_StarGiftWithdrawalUrl = $MadelineProto->payments->getStarGiftWithdrawalUrl(stargift: $InputSavedStarGift, tmp_password: 'bytes', );
```
