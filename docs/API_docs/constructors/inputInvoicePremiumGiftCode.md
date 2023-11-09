---
title: "inputInvoicePremiumGiftCode"
description: "inputInvoicePremiumGiftCode attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputInvoicePremiumGiftCode  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|purpose|[InputStorePaymentPurpose](/API_docs/types/InputStorePaymentPurpose.html) | Yes|
|option|[PremiumGiftCodeOption](/API_docs/types/PremiumGiftCodeOption.html) | Yes|



### Type: [InputInvoice](/API_docs/types/InputInvoice.html)


### Example:

```
$inputInvoicePremiumGiftCode = ['_' => 'inputInvoicePremiumGiftCode', 'purpose' => InputStorePaymentPurpose, 'option' => PremiumGiftCodeOption];
```  
