---
title: "payments.getStarsGiftOptions"
description: "Obtain a list of [Telegram Stars gift options »](https://core.telegram.org/api/stars#buying-or-gifting-stars) as [starsGiftOption](../constructors/starsGiftOption.html) constructors."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getStarsGiftOptions.html
---
# Method: payments.getStarsGiftOptions
[Back to methods index](index.html)



Obtain a list of [Telegram Stars gift options »](https://core.telegram.org/api/stars#buying-or-gifting-stars) as [starsGiftOption](../constructors/starsGiftOption.html) constructors.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Receiver of the gift (optional). | Optional|


### Return type: [Vector\_of\_StarsGiftOption](/API_docs/types/StarsGiftOption.html)

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

$Vector_of_StarsGiftOption = $MadelineProto->payments->getStarsGiftOptions(user_id: $InputUser, );
```

