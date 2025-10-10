---
title: "payments.upgradeStarGift"
description: "Upgrade a [gift](https://core.telegram.org/api/gifts) to a [collectible gift](https://core.telegram.org/api/gifts#collectible-gifts): can only be used if the upgrade was already paid by the gift sender; see [here »](https://core.telegram.org/api/gifts#upgrade-a-gift-to-a-collectible-gift) for more info on the full flow (including the different flow to use in case the upgrade was not paid by the gift sender)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_upgradeStarGift.html
---
# Method: payments.upgradeStarGift
[Back to methods index](index.html)



Upgrade a [gift](https://core.telegram.org/api/gifts) to a [collectible gift](https://core.telegram.org/api/gifts#collectible-gifts): can only be used if the upgrade was already paid by the gift sender; see [here »](https://core.telegram.org/api/gifts#upgrade-a-gift-to-a-collectible-gift) for more info on the full flow (including the different flow to use in case the upgrade was not paid by the gift sender).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|keep\_original\_details|[Bool](/API_docs/types/Bool.html) | Set this flag to keep the original gift text, sender and receiver in the upgraded gift as a [starGiftAttributeOriginalDetails](../constructors/starGiftAttributeOriginalDetails.html) attribute. | Optional|
|stargift|[InputSavedStarGift](/API_docs/types/InputSavedStarGift.html) | The gift to upgrade | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->payments->upgradeStarGift(keep_original_details: $Bool, stargift: $InputSavedStarGift, );
```

