---
title: "payments.getStarGifts"
description: "Get a list of available [gifts, see here »](https://core.telegram.org/api/gifts) for more info."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getStarGifts.html
---
# Method: payments.getStarGifts
[Back to methods index](index.html)



Get a list of available [gifts, see here »](https://core.telegram.org/api/gifts) for more info.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) |  | Optional|


### Return type: [payments.StarGifts](/API_docs/types/payments.StarGifts.html)

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

$payments_StarGifts = $MadelineProto->payments->getStarGifts(hash: [$long\|string, $long\|string], );
```

