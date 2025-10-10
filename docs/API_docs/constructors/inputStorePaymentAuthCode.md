---
title: "inputStorePaymentAuthCode"
description: "Indicates payment for a login code."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStorePaymentAuthCode  
[Back to constructors index](/API_docs/constructors/index.html)



Indicates payment for a login code.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|restore|[Bool](/API_docs/types/Bool.html) | Optional|Set this flag to restore a previously made purchase.|
|phone\_number|[string](/API_docs/types/string.html) | Yes|Phone number.|
|phone\_code\_hash|[string](/API_docs/types/string.html) | Yes|`phone_code_hash` returned by [auth.sendCode](../methods/auth.sendCode.html).|
|currency|[string](/API_docs/types/string.html) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|amount|[long](/API_docs/types/long.html) | Yes|Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|



### Type: [InputStorePaymentPurpose](/API_docs/types/InputStorePaymentPurpose.html)


### Example:

```
$inputStorePaymentAuthCode = ['_' => 'inputStorePaymentAuthCode', 'restore' => Bool, 'phone_number' => 'string', 'phone_code_hash' => 'string', 'currency' => 'string', 'amount' => long];
```  
