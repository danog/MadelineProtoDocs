---
title: "payments.paymentVerificationNeeded"
description: "Payment was not successful, additional verification is needed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_paymentVerificationNeeded.html
---
# Constructor: payments.paymentVerificationNeeded  
[Back to constructors index](/API_docs/constructors/index.html)



Payment was not successful, additional verification is needed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](/API_docs/types/string.html) | Yes|URL for additional payment credentials verification|



### Type: [payments.PaymentResult](/API_docs/types/payments.PaymentResult.html)


### Example:

```
$payments_paymentVerificationNeeded = ['_' => 'payments.paymentVerificationNeeded', 'url' => 'string'];
```  
