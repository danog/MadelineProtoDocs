---
title: "inputInvoiceStarGiftResale"
description: "Used to buy a collectible gift currently up on resale, see here for more info on the full flow."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputInvoiceStarGiftResale  
[Back to constructors index](/API_docs/constructors/index.html)



Used to buy a [collectible gift](https://core.telegram.org/api/gifts#collectible-gifts) currently up on resale, see [here](https://core.telegram.org/api/gifts#reselling-collectible-gifts) for more info on the full flow.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|ton|[Bool](/API_docs/types/Bool.html) | Optional|Buy the gift using TON.|
|slug|[string](/API_docs/types/string.html) | Yes|Slug of the gift to buy.|
|to\_id|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|The receiver of the gift.|



### Type: [InputInvoice](/API_docs/types/InputInvoice.html)


### Example:

```
$inputInvoiceStarGiftResale = ['_' => 'inputInvoiceStarGiftResale', 'ton' => Bool, 'slug' => 'string', 'to_id' => InputPeer];
```  
