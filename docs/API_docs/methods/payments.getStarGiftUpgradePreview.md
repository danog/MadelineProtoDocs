---
title: "payments.getStarGiftUpgradePreview"
description: "Obtain a preview of the possible attributes (chosen randomly) a [gift »](https://core.telegram.org/api/gifts) can receive after upgrading it to a [collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts), see [here »](https://core.telegram.org/api/gifts#collectible-gifts) for more info."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getStarGiftUpgradePreview.html
---
# Method: payments.getStarGiftUpgradePreview
[Back to methods index](index.html)



Obtain a preview of the possible attributes (chosen randomly) a [gift »](https://core.telegram.org/api/gifts) can receive after upgrading it to a [collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts), see [here »](https://core.telegram.org/api/gifts#collectible-gifts) for more info.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|gift\_id|[long](/API_docs/types/long.html) | The gift to upgrade. | Yes|


### Return type: [payments.StarGiftUpgradePreview](/API_docs/types/payments.StarGiftUpgradePreview.html)

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

$payments_StarGiftUpgradePreview = $MadelineProto->payments->getStarGiftUpgradePreview(gift_id: $long, );
```

