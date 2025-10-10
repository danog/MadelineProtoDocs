---
title: "inputStorePaymentStarsTopup"
description: "Used to top up the Telegram Stars balance of the current account."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStorePaymentStarsTopup  
[Back to constructors index](/API_docs/constructors/index.html)



Used to top up the [Telegram Stars balance](https://core.telegram.org/api/stars) of the current account.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|stars|[long](/API_docs/types/long.html) | Yes|Amount of stars to topup|
|currency|[string](/API_docs/types/string.html) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|amount|[long](/API_docs/types/long.html) | Yes|Total price in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|
|spend\_purpose\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|Should be populated with the peer where the topup process was initiated due to low funds (i.e. a bot for bot payments, a channel for paid media/reactions, etc); leave this flag unpopulated if the topup flow was not initated when attempting to spend more Stars than currently available on the account's balance.|



### Type: [InputStorePaymentPurpose](/API_docs/types/InputStorePaymentPurpose.html)


### Example:

```
$inputStorePaymentStarsTopup = ['_' => 'inputStorePaymentStarsTopup', 'stars' => long, 'currency' => 'string', 'amount' => long, 'spend_purpose_peer' => InputPeer];
```  
