---
title: "messageActionGiftPremium"
description: "Info about a gifted Telegram Premium subscription"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGiftPremium  
[Back to constructors index](/API_docs/constructors/index.html)



Info about a gifted Telegram Premium subscription

This service message should be displayed below the appropriate sticker from the [inputStickerSetPremiumGifts »](../constructors/inputStickerSetPremiumGifts.html) [stickerset »](https://core.telegram.org/api/stickers#stickersets):

- If `months == 1`, choose the sticker with emoji equal to "1️⃣"
- If `months == 3`, choose the sticker with emoji equal to "2️⃣"
- If `months == 6`, choose the sticker with emoji equal to "3️⃣"
- If `months == 12`, choose the sticker with emoji equal to "4️⃣"
- If `months == 24`, choose the sticker with emoji equal to "5️⃣"
- Otherwise, fallback to the sticker with emoji equal to "1️⃣"

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|currency|[string](/API_docs/types/string.html) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|amount|[long](/API_docs/types/long.html) | Yes|Price of the gift in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|
|months|[int](/API_docs/types/int.html) | Yes|Duration of the gifted Telegram Premium subscription.|
|crypto\_currency|[string](/API_docs/types/string.html) | Optional|If the gift was bought using a cryptocurrency, the cryptocurrency name.|
|crypto\_amount|[long](/API_docs/types/long.html) | Optional|If the gift was bought using a cryptocurrency, price of the gift in the smallest units of a cryptocurrency.|
|message|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Optional|Message attached with the gift|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionGiftPremium = ['_' => 'messageActionGiftPremium', 'currency' => 'string', 'amount' => long, 'months' => int, 'crypto_currency' => 'string', 'crypto_amount' => long, 'message' => TextWithEntities];
```  
