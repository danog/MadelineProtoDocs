---
title: "inputInvoicePremiumGiftStars"
description: "Used to gift a Telegram Premium subscription to another user, paying with Telegram Stars."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputInvoicePremiumGiftStars  
[Back to constructors index](/API_docs/constructors/index.html)



Used to gift a [Telegram Premium](https://core.telegram.org/api/premium) subscription to another user, paying with [Telegram Stars](https://core.telegram.org/api/stars).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|Who will receive the gifted subscription.|
|months|[int](/API_docs/types/int.html) | Yes|Duration of the subscription in months, must be one of the options with `currency == "XTR"` returned by [payments.getPremiumGiftCodeOptions](../methods/payments.getPremiumGiftCodeOptions.html).|
|message|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Optional|Message attached with the gift.|



### Type: [InputInvoice](/API_docs/types/InputInvoice.html)


### Example:

```
$inputInvoicePremiumGiftStars = ['_' => 'inputInvoicePremiumGiftStars', 'user_id' => InputUser, 'months' => int, 'message' => TextWithEntities];
```  
