---
title: "inputStorePaymentPremiumGiftCode"
description: "Used to gift Telegram Premium subscriptions only to some specific subscribers of a channel or to some of our contacts, see here » for more info on giveaways and gifts."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStorePaymentPremiumGiftCode  
[Back to constructors index](/API_docs/constructors/index.html)



Used to gift [Telegram Premium](https://core.telegram.org/api/premium) subscriptions only to some specific subscribers of a channel or to some of our contacts, see [here »](https://core.telegram.org/api/giveaways) for more info on giveaways and gifts.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|users|Array of [Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Yes|The users that will receive the [Telegram Premium](https://core.telegram.org/api/premium) subscriptions.|
|boost\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|If set, the gifts will be sent on behalf of a channel we are an admin of, which will also assign some [boosts](https://core.telegram.org/api/boost) to it. Otherwise, the gift will be sent directly from the currently logged in users, and we will gain some extra [boost slots](https://core.telegram.org/api/boost). See [here »](https://core.telegram.org/api/giveaways) for more info on giveaways and gifts.|
|currency|[string](/API_docs/types/string.html) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|amount|[long](/API_docs/types/long.html) | Yes|Total price in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|



### Type: [InputStorePaymentPurpose](/API_docs/types/InputStorePaymentPurpose.html)


### Example:

```
$inputStorePaymentPremiumGiftCode = ['_' => 'inputStorePaymentPremiumGiftCode', 'users' => [InputUser, InputUser], 'boost_peer' => InputPeer, 'currency' => 'string', 'amount' => long];
```  
