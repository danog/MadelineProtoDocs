---
title: "payments.paymentReceiptStars"
description: "payments.paymentReceiptStars attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_paymentReceiptStars.html
---
# Constructor: payments.paymentReceiptStars  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|date|[int](/API_docs/types/int.html) | Yes|
|bot\_id|[long](/API_docs/types/long.html) | Yes|
|title|[string](/API_docs/types/string.html) | Yes|
|description|[string](/API_docs/types/string.html) | Yes|
|photo|[WebDocument](/API_docs/types/WebDocument.html) | Optional|
|invoice|[Invoice](/API_docs/types/Invoice.html) | Yes|
|currency|[string](/API_docs/types/string.html) | Yes|
|total\_amount|[long](/API_docs/types/long.html) | Yes|
|transaction\_id|[string](/API_docs/types/string.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [payments.PaymentReceipt](/API_docs/types/payments.PaymentReceipt.html)


### Example:

```
$payments_paymentReceiptStars = ['_' => 'payments.paymentReceiptStars', 'date' => int, 'bot_id' => long, 'title' => 'string', 'description' => 'string', 'photo' => WebDocument, 'invoice' => Invoice, 'currency' => 'string', 'total_amount' => long, 'transaction_id' => 'string', 'users' => [User, User]];
```  
