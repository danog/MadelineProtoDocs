---
title: "starsGiveawayOption"
description: "Contains info about a Telegram Star giveaway option."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starsGiveawayOption  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about a [Telegram Star giveaway](https://core.telegram.org/api/giveaways#star-giveaways) option.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|extended|[Bool](/API_docs/types/Bool.html) | Optional|If set, this option must only be shown in the full list of giveaway options (i.e. they must be added to the list only when the user clicks on the expand button).|
|default|[Bool](/API_docs/types/Bool.html) | Optional|If set, this option must be pre-selected by default in the option list.|
|stars|[long](/API_docs/types/long.html) | Yes|The number of Telegram Stars that will be distributed among winners|
|yearly\_boosts|[int](/API_docs/types/int.html) | Yes|Number of times the chat will be boosted for one year if the [inputStorePaymentStarsGiveaway](../constructors/inputStorePaymentStarsGiveaway.html).`boost_peer` flag is populated|
|store\_product|[string](/API_docs/types/string.html) | Optional|Identifier of the store product associated with the option, official apps only.|
|currency|[string](/API_docs/types/string.html) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|amount|[long](/API_docs/types/long.html) | Yes|Total price in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|
|winners|Array of [StarsGiveawayWinnersOption](/API_docs/types/StarsGiveawayWinnersOption.html) | Yes|Allowed options for the number of giveaway winners.|



### Type: [StarsGiveawayOption](/API_docs/types/StarsGiveawayOption.html)


### Example:

```
$starsGiveawayOption = ['_' => 'starsGiveawayOption', 'extended' => Bool, 'default' => Bool, 'stars' => long, 'yearly_boosts' => int, 'store_product' => 'string', 'currency' => 'string', 'amount' => long, 'winners' => [StarsGiveawayWinnersOption, StarsGiveawayWinnersOption]];
```  
