---
title: "inputInvoicePremiumGiftCode"
description: "Used if the user wishes to start a channel giveaway or send some giftcodes to members of a channel, in exchange for boosts."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputInvoicePremiumGiftCode  
[Back to constructors index](/API_docs/constructors/index.html)



Used if the user wishes to start a channel [giveaway](https://core.telegram.org/api/giveaways) or send some [giftcodes](https://core.telegram.org/api/giveaways) to members of a channel, in exchange for [boosts](https://core.telegram.org/api/boost).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|purpose|[InputStorePaymentPurpose](/API_docs/types/InputStorePaymentPurpose.html) | Yes|Should be populated with [inputStorePaymentPremiumGiveaway](../constructors/inputStorePaymentPremiumGiveaway.html) for [giveaways](https://core.telegram.org/api/giveaways) and [inputStorePaymentPremiumGiftCode](../constructors/inputStorePaymentPremiumGiftCode.html) for [gifts](https://core.telegram.org/api/giveaways).|
|option|[PremiumGiftCodeOption](/API_docs/types/PremiumGiftCodeOption.html) | Yes|Should be populated with one of the giveaway options returned by [payments.getPremiumGiftCodeOptions](../methods/payments.getPremiumGiftCodeOptions.html), see the [giveaways »](https://core.telegram.org/api/giveaways) documentation for more info.|



### Type: [InputInvoice](/API_docs/types/InputInvoice.html)


### Example:

```
$inputInvoicePremiumGiftCode = ['_' => 'inputInvoicePremiumGiftCode', 'purpose' => InputStorePaymentPurpose, 'option' => PremiumGiftCodeOption];
```  
