---
title: "payments.paymentFormStars"
description: "Represents a payment form, for payments to be using Telegram Stars, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_paymentFormStars.html
---
# Constructor: payments.paymentFormStars  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a payment form, for payments to be using [Telegram Stars, see here »](https://core.telegram.org/api/stars) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|form\_id|[long](/API_docs/types/long.html) | Yes|Form ID.|
|bot\_id|[long](/API_docs/types/long.html) | Yes|Bot ID.|
|title|[string](/API_docs/types/string.html) | Yes|Form title|
|description|[string](/API_docs/types/string.html) | Yes|Description|
|photo|[WebDocument](/API_docs/types/WebDocument.html) | Optional|Product photo|
|invoice|[Invoice](/API_docs/types/Invoice.html) | Yes|Invoice|
|users|Array of [User](/API_docs/types/User.html) | Yes|Info about users mentioned in the other fields.|



### Type: [payments.PaymentForm](/API_docs/types/payments.PaymentForm.html)


### Example:

```
$payments_paymentFormStars = ['_' => 'payments.paymentFormStars', 'form_id' => long, 'bot_id' => long, 'title' => 'string', 'description' => 'string', 'photo' => WebDocument, 'invoice' => Invoice, 'users' => [User, User]];
```  
