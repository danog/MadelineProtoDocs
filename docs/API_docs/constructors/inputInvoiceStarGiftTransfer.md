---
title: "inputInvoiceStarGiftTransfer"
description: "inputInvoiceStarGiftTransfer attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputInvoiceStarGiftTransfer  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|stargift|[InputSavedStarGift](/API_docs/types/InputSavedStarGift.html) | Yes|
|to\_id|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|



### Type: [InputInvoice](/API_docs/types/InputInvoice.html)


### Example:

```
$inputInvoiceStarGiftTransfer = ['_' => 'inputInvoiceStarGiftTransfer', 'stargift' => InputSavedStarGift, 'to_id' => InputPeer];
```  
