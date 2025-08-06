---
title: "payments.getStarsTopupOptions"
description: "Obtain a list of [Telegram Stars topup options »](https://core.telegram.org/api/stars#buying-or-gifting-stars) as [starsTopupOption](../constructors/starsTopupOption.html) constructors."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getStarsTopupOptions.html
---
# Method: payments.getStarsTopupOptions
[Back to methods index](index.html)



Obtain a list of [Telegram Stars topup options »](https://core.telegram.org/api/stars#buying-or-gifting-stars) as [starsTopupOption](../constructors/starsTopupOption.html) constructors.



### Return type: [Vector\_of\_StarsTopupOption](/API_docs/types/StarsTopupOption.html)

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

$Vector_of_StarsTopupOption = $MadelineProto->payments->getStarsTopupOptions();
```

