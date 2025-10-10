---
title: "messageActionGiftTon"
description: "You were gifted some toncoins."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGiftTon  
[Back to constructors index](/API_docs/constructors/index.html)



You were gifted some toncoins.

This service message should be displayed below the appropriate sticker from the [inputStickerSetTonGifts »](../constructors/inputStickerSetTonGifts.html) [stickerset »](https://core.telegram.org/api/stickers#stickersets):

- If `crypto_amount <= 10_000_000_000`, choose the sticker with emoji equal to "2️⃣"
- If `crypto_amount <= 50_000_000_000`, choose the sticker with emoji equal to "1️⃣"
- Otherwise, choose the sticker with emoji equal to "3️⃣"

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|currency|[string](/API_docs/types/string.html) | Yes|Name of a localized FIAT currency.|
|amount|[long](/API_docs/types/long.html) | Yes|FIAT currency equivalent (in the currency specified in `currency`) of the amount specified in `crypto_amount`.|
|crypto\_currency|[string](/API_docs/types/string.html) | Yes|Name of the cryptocurrency.|
|crypto\_amount|[long](/API_docs/types/long.html) | Yes|Amount in the smallest unit of the cryptocurrency (for TONs, one billionth of a ton, AKA a nanoton).|
|transaction\_id|[string](/API_docs/types/string.html) | Optional|Transaction ID.|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionGiftTon = ['_' => 'messageActionGiftTon', 'currency' => 'string', 'amount' => long, 'crypto_currency' => 'string', 'crypto_amount' => long, 'transaction_id' => 'string'];
```  
