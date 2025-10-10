---
title: "inputInvoiceStarGiftTransfer"
description: "Used to pay to transfer a collectible gift to another peer, see the gifts » documentation for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputInvoiceStarGiftTransfer  
[Back to constructors index](/API_docs/constructors/index.html)



Used to [pay to transfer a collectible gift to another peer](https://core.telegram.org/api/gifts#transferring-collectible-gifts), see the [gifts »](https://core.telegram.org/api/gifts#transferring-collectible-gifts) documentation for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|stargift|[InputSavedStarGift](/API_docs/types/InputSavedStarGift.html) | Yes|The identifier of the received gift|
|to\_id|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|The destination peer|



### Type: [InputInvoice](/API_docs/types/InputInvoice.html)


### Example:

```
$inputInvoiceStarGiftTransfer = ['_' => 'inputInvoiceStarGiftTransfer', 'stargift' => InputSavedStarGift, 'to_id' => InputPeer];
```  
