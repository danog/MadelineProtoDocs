---
title: "payments.convertStarGift"
description: "Convert a [received gift »](https://core.telegram.org/api/gifts) into Telegram Stars: this will permanently destroy the gift, converting it into [starGift](../constructors/starGift.html).`convert_stars` [Telegram Stars](https://core.telegram.org/api/stars), added to the user's balance."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_convertStarGift.html
---
# Method: payments.convertStarGift
[Back to methods index](index.html)



Convert a [received gift »](https://core.telegram.org/api/gifts) into Telegram Stars: this will permanently destroy the gift, converting it into [starGift](../constructors/starGift.html).`convert_stars` [Telegram Stars](https://core.telegram.org/api/stars), added to the user's balance.

Note that [starGift](../constructors/starGift.html).`convert_stars` will be less than the buying price ([starGift](../constructors/starGift.html).`stars`) of the gift if it was originally bought using Telegram Stars bought a long time ago.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|stargift|[InputSavedStarGift](/API_docs/types/InputSavedStarGift.html) |  | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->payments->convertStarGift(stargift: $InputSavedStarGift, );
```

