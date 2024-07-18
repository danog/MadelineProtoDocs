---
title: "messageActionPaymentRefunded"
description: "messageActionPaymentRefunded attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionPaymentRefunded  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[long](/API_docs/types/long.html) | Yes|
|currency|[string](/API_docs/types/string.html) | Yes|
|total\_amount|[long](/API_docs/types/long.html) | Yes|
|payload|[bytes](/API_docs/types/bytes.html) | Optional|
|charge|[PaymentCharge](/API_docs/types/PaymentCharge.html) | Yes|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionPaymentRefunded = ['_' => 'messageActionPaymentRefunded', 'peer' => long, 'currency' => 'string', 'total_amount' => long, 'payload' => 'bytes', 'charge' => PaymentCharge];
```  
