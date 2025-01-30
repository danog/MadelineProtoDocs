---
title: "messageActionGiftStars"
description: "You gifted or were gifted some Telegram Stars."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGiftStars  
[Back to constructors index](/API_docs/constructors/index.html)



You gifted or were gifted some [Telegram Stars](https://core.telegram.org/api/stars).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|currency|[string](/API_docs/types/string.html) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|amount|[long](/API_docs/types/long.html) | Yes|Price of the gift in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|
|stars|[long](/API_docs/types/long.html) | Yes|Amount of gifted stars|
|crypto\_currency|[string](/API_docs/types/string.html) | Optional|If the gift was bought using a cryptocurrency, the cryptocurrency name.|
|crypto\_amount|[long](/API_docs/types/long.html) | Optional|If the gift was bought using a cryptocurrency, price of the gift in the smallest units of a cryptocurrency.|
|transaction\_id|[string](/API_docs/types/string.html) | Optional|Identifier of the transaction, only visible to the receiver of the gift.|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionGiftStars = ['_' => 'messageActionGiftStars', 'currency' => 'string', 'amount' => long, 'stars' => long, 'crypto_currency' => 'string', 'crypto_amount' => long, 'transaction_id' => 'string'];
```  
