---
title: "messageActionGiftPremium"
description: "Info about a gifted Telegram Premium subscription"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGiftPremium  
[Back to constructors index](/API_docs/constructors/index.html)



Info about a gifted Telegram Premium subscription

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|currency|[string](/API_docs/types/string.html) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|amount|[long](/API_docs/types/long.html) | Yes|Price of the gift in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|
|months|[int](/API_docs/types/int.html) | Yes|Duration of the gifted Telegram Premium subscription|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionGiftPremium = ['_' => 'messageActionGiftPremium', 'currency' => 'string', 'amount' => long, 'months' => int];
```  
