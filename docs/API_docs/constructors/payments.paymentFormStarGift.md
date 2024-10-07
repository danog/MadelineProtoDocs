---
title: "payments.paymentFormStarGift"
description: "payments.paymentFormStarGift attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_paymentFormStarGift.html
---
# Constructor: payments.paymentFormStarGift  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|form\_id|[long](/API_docs/types/long.html) | Yes|
|invoice|[Invoice](/API_docs/types/Invoice.html) | Yes|



### Type: [payments.PaymentForm](/API_docs/types/payments.PaymentForm.html)


### Example:

```
$payments_paymentFormStarGift = ['_' => 'payments.paymentFormStarGift', 'form_id' => long, 'invoice' => Invoice];
```  
