---
title: "payments.botCancelStarsSubscription"
description: "Cancel a [bot subscription](https://core.telegram.org/api/subscriptions#bot-subscriptions)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_botCancelStarsSubscription.html
---
# Method: payments.botCancelStarsSubscription
[Back to methods index](index.html)



Cancel a [bot subscription](https://core.telegram.org/api/subscriptions#bot-subscriptions)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|restore|[Bool](/API_docs/types/Bool.html) | If **not** set, disables autorenewal of the subscriptions, and prevents the user from reactivating the subscription once the current period expires: a subscription cancelled by the bot will have the [starsSubscription](../constructors/starsSubscription.html).`bot_canceled` flag set.  <br>The bot can can partially undo this operation by setting this flag: this will allow the user to reactivate the subscription. | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The ID of the user whose subscription should be (un)cancelled | Optional|
|charge\_id|[string](/API_docs/types/string.html) | The `provider_charge_id` from the [messageActionPaymentSentMe](../constructors/messageActionPaymentSentMe.html) service message sent to the bot for the first subscription payment. | Optional|


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

$Bool = $MadelineProto->payments->botCancelStarsSubscription(restore: $Bool, user_id: $InputUser, charge_id: 'string', );
```

