---
title: "inputStorePaymentStarsGift"
description: "Used to gift Telegram Stars to a friend."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStorePaymentStarsGift  
[Back to constructors index](/API_docs/constructors/index.html)



Used to gift [Telegram Stars](https://core.telegram.org/api/stars) to a friend.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|The user to which the stars should be gifted.|
|stars|[long](/API_docs/types/long.html) | Yes|Amount of stars to gift|
|currency|[string](/API_docs/types/string.html) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|amount|[long](/API_docs/types/long.html) | Yes|Total price in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|



### Type: [InputStorePaymentPurpose](/API_docs/types/InputStorePaymentPurpose.html)


### Example:

```
$inputStorePaymentStarsGift = ['_' => 'inputStorePaymentStarsGift', 'user_id' => InputUser, 'stars' => long, 'currency' => 'string', 'amount' => long];
```  
