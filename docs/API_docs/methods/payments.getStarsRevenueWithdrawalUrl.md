---
title: "payments.getStarsRevenueWithdrawalUrl"
description: "Withdraw funds from a channel or bot's [star balance »](https://core.telegram.org/api/stars#withdrawing-revenue)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getStarsRevenueWithdrawalUrl.html
---
# Method: payments.getStarsRevenueWithdrawalUrl
[Back to methods index](index.html)



Withdraw funds from a channel or bot's [star balance »](https://core.telegram.org/api/stars#withdrawing-revenue).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|ton|[Bool](/API_docs/types/Bool.html) | If set, withdraws channel/ad revenue in TON. | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Channel or bot from which to withdraw funds. | Optional|
|amount|[long](/API_docs/types/long.html) | The amount of stars or nanotons to withdraw. | Optional|
|password|[InputCheckPasswordSRP](/API_docs/types/InputCheckPasswordSRP.html) | 2FA password, see [here »](https://core.telegram.org/api/srp#using-the-2fa-password) for more info. | Yes|


### Return type: [payments.StarsRevenueWithdrawalUrl](/API_docs/types/payments.StarsRevenueWithdrawalUrl.html)

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

$payments_StarsRevenueWithdrawalUrl = $MadelineProto->payments->getStarsRevenueWithdrawalUrl(ton: $Bool, peer: $InputPeer, amount: $long, password: $InputCheckPasswordSRP, );
```

