---
title: "inputInvoiceStarGift"
description: "inputInvoiceStarGift attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputInvoiceStarGift  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hide\_name|[Bool](/API_docs/types/Bool.html) | Optional|
|include\_upgrade|[Bool](/API_docs/types/Bool.html) | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|
|gift\_id|[long](/API_docs/types/long.html) | Yes|
|message|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Optional|



### Type: [InputInvoice](/API_docs/types/InputInvoice.html)


### Example:

```
$inputInvoiceStarGift = ['_' => 'inputInvoiceStarGift', 'hide_name' => Bool, 'include_upgrade' => Bool, 'user_id' => InputUser, 'gift_id' => long, 'message' => TextWithEntities];
```  
