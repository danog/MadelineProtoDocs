---
title: "messageActionGiftCode"
description: "Contains a Telegram Premium giftcode link."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGiftCode  
[Back to constructors index](/API_docs/constructors/index.html)



Contains a [Telegram Premium giftcode link](https://core.telegram.org/api/links#premium-giftcode-links).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|via\_giveaway|[Bool](/API_docs/types/Bool.html) | Optional|If set, this gift code was received from a [giveaway »](https://core.telegram.org/api/giveaways) started by a channel we're subscribed to.|
|unclaimed|[Bool](/API_docs/types/Bool.html) | Optional|If set, the link was not [redeemed](https://core.telegram.org/api/links#premium-giftcode-links) yet.|
|boost\_peer|[Peer](/API_docs/types/Peer.html) | Optional|Identifier of the channel that created the gift code [either directly or through a giveaway](https://core.telegram.org/api/giveaways): if we import this giftcode link, we will also automatically [boost](https://core.telegram.org/api/boost) this channel.|
|months|[int](/API_docs/types/int.html) | Yes|Duration in months of the gifted [Telegram Premium subscription](https://core.telegram.org/api/premium).|
|slug|[string](/API_docs/types/string.html) | Yes|Slug of the [Telegram Premium giftcode link](https://core.telegram.org/api/links#premium-giftcode-links)|
|currency|[string](/API_docs/types/string.html) | Optional|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|amount|[long](/API_docs/types/long.html) | Optional|Total price in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|
|crypto\_currency|[string](/API_docs/types/string.html) | Optional|If set, the gift was made using the specified cryptocurrency.|
|crypto\_amount|[long](/API_docs/types/long.html) | Optional|If `crypto_currency` is set, contains the paid amount, in the smallest units of the cryptocurrency.|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionGiftCode = ['_' => 'messageActionGiftCode', 'via_giveaway' => Bool, 'unclaimed' => Bool, 'boost_peer' => Peer, 'months' => int, 'slug' => 'string', 'currency' => 'string', 'amount' => long, 'crypto_currency' => 'string', 'crypto_amount' => long];
```  
