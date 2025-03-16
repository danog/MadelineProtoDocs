---
title: "inputInvoicePremiumGiftStars"
description: "inputInvoicePremiumGiftStars attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputInvoicePremiumGiftStars  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|
|months|[int](/API_docs/types/int.html) | Yes|
|message|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Optional|



### Type: [InputInvoice](/API_docs/types/InputInvoice.html)


### Example:

```
$inputInvoicePremiumGiftStars = ['_' => 'inputInvoicePremiumGiftStars', 'user_id' => InputUser, 'months' => int, 'message' => TextWithEntities];
```  
