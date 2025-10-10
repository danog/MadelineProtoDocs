---
title: "payments.getUniqueStarGift"
description: "Obtain info about a [collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts) using a slug obtained from a [collectible gift link »](https://core.telegram.org/api/links#collectible-gift-link)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getUniqueStarGift.html
---
# Method: payments.getUniqueStarGift
[Back to methods index](index.html)



Obtain info about a [collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts) using a slug obtained from a [collectible gift link »](https://core.telegram.org/api/links#collectible-gift-link).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|slug|[string](/API_docs/types/string.html) | The slug. | Optional|


### Return type: [payments.UniqueStarGift](/API_docs/types/payments.UniqueStarGift.html)

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

$payments_UniqueStarGift = $MadelineProto->payments->getUniqueStarGift(slug: 'string', );
```

