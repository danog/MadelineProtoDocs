---
title: "payments.paymentFormStars"
description: "payments.paymentFormStars attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_paymentFormStars.html
---
# Constructor: payments.paymentFormStars  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|form\_id|[long](/API_docs/types/long.html) | Yes|
|bot\_id|[long](/API_docs/types/long.html) | Yes|
|title|[string](/API_docs/types/string.html) | Yes|
|description|[string](/API_docs/types/string.html) | Yes|
|photo|[WebDocument](/API_docs/types/WebDocument.html) | Optional|
|invoice|[Invoice](/API_docs/types/Invoice.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [payments.PaymentForm](/API_docs/types/payments.PaymentForm.html)


### Example:

```
$payments_paymentFormStars = ['_' => 'payments.paymentFormStars', 'form_id' => long, 'bot_id' => long, 'title' => 'string', 'description' => 'string', 'photo' => WebDocument, 'invoice' => Invoice, 'users' => [User, User]];
```  
