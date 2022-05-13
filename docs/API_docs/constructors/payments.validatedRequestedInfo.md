---
title: "payments.validatedRequestedInfo"
description: "Validated user-provided info"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_validatedRequestedInfo.html
---
# Constructor: payments.validatedRequestedInfo  
[Back to constructors index](/API_docs/constructors/index.html)



Validated user-provided info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](/API_docs/types/string.html) | Optional|ID|
|shipping\_options|Array of [ShippingOption](/API_docs/types/ShippingOption.html) | Optional|Shipping options|



### Type: [payments.ValidatedRequestedInfo](/API_docs/types/payments.ValidatedRequestedInfo.html)


### Example:

```
$payments_validatedRequestedInfo = ['_' => 'payments.validatedRequestedInfo', 'id' => 'string', 'shipping_options' => [ShippingOption, ShippingOption]];
```  
