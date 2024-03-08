---
title: "inputStorePaymentPremiumGiveaway"
description: "Used to pay for a giveaway, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStorePaymentPremiumGiveaway  
[Back to constructors index](/API_docs/constructors/index.html)



Used to pay for a [giveaway, see here »](https://core.telegram.org/api/giveaways) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|only\_new\_subscribers|[Bool](/API_docs/types/Bool.html) | Optional|If set, only new subscribers starting from the giveaway creation date will be able to participate to the giveaway.|
|winners\_are\_visible|[Bool](/API_docs/types/Bool.html) | Optional|If set, giveaway winners are public and will be listed in a [messageMediaGiveawayResults](../constructors/messageMediaGiveawayResults.html) message that will be automatically sent to the channel once the giveaway ends.|
|boost\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|The channel starting the giveaway, that the user must join to participate, that will receive the giveaway [boosts](https://core.telegram.org/api/boost); see [here »](https://core.telegram.org/api/giveaways) for more info on giveaways.|
|additional\_peers|Array of [Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|Additional channels that the user must join to participate to the giveaway can be specified here.|
|countries\_iso2|Array of [string](/API_docs/types/string.html) | Optional|The set of users that can participate to the giveaway can be restricted by passing here an explicit whitelist of up to [giveaway\_countries\_max](https://core.telegram.org/api/config#giveaway-countries-max) countries, specified as two-letter ISO 3166-1 alpha-2 country codes.|
|prize\_description|[string](/API_docs/types/string.html) | Optional|Can contain a textual description of additional giveaway prizes.|
|until\_date|[int](/API_docs/types/int.html) | Yes|The end date of the giveaway, must be at most [giveaway\_period\_max](https://core.telegram.org/api/config#giveaway-period-max) seconds in the future; see [here »](https://core.telegram.org/api/giveaways) for more info on giveaways.|
|currency|[string](/API_docs/types/string.html) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|amount|[long](/API_docs/types/long.html) | Yes|Total price in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|



### Type: [InputStorePaymentPurpose](/API_docs/types/InputStorePaymentPurpose.html)


### Example:

```
$inputStorePaymentPremiumGiveaway = ['_' => 'inputStorePaymentPremiumGiveaway', 'only_new_subscribers' => Bool, 'winners_are_visible' => Bool, 'boost_peer' => InputPeer, 'additional_peers' => [InputPeer, InputPeer], 'countries_iso2' => ['string', 'string'], 'prize_description' => 'string', 'until_date' => int, 'currency' => 'string', 'amount' => long];
```  
