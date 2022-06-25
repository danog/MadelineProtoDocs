---
title: "inputInvoiceMessage"
description: "inputInvoiceMessage attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputInvoiceMessage  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Yes|



### Type: [InputInvoice](/API_docs/types/InputInvoice.html)


### Example:

```
$inputInvoiceMessage = ['_' => 'inputInvoiceMessage', 'peer' => InputPeer, 'msg_id' => int];
```  
