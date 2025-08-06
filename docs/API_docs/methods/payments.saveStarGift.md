---
title: "payments.saveStarGift"
description: "Display or remove a [received gift »](https://core.telegram.org/api/gifts) from our profile."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_saveStarGift.html
---
# Method: payments.saveStarGift
[Back to methods index](index.html)



Display or remove a [received gift »](https://core.telegram.org/api/gifts) from our profile.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|unsave|[Bool](/API_docs/types/Bool.html) | If set, hides the gift from our profile. | Optional|
|stargift|[InputSavedStarGift](/API_docs/types/InputSavedStarGift.html) |  | Yes|


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

$Bool = $MadelineProto->payments->saveStarGift(unsave: $Bool, stargift: $InputSavedStarGift, );
```

