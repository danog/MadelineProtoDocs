---
title: "inputInvoiceMessage"
description: "An invoice contained in a messageMediaInvoice message or paid media »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputInvoiceMessage  
[Back to constructors index](/API_docs/constructors/index.html)



An invoice contained in a [messageMediaInvoice](../constructors/messageMediaInvoice.html) message or [paid media »](https://core.telegram.org/api/paid-media).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|Chat where the invoice/paid media was sent|
|msg\_id|[int](/API_docs/types/int.html) | Yes|Message ID|



### Type: [InputInvoice](/API_docs/types/InputInvoice.html)


### Example:

```
$inputInvoiceMessage = ['_' => 'inputInvoiceMessage', 'peer' => InputPeer, 'msg_id' => int];
```  
