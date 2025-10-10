---
title: "inputInvoiceStarGiftUpgrade"
description: "Used to pay to upgrade a Gift to a collectible gift, see the collectible gifts » documentation for more info on the full flow."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputInvoiceStarGiftUpgrade  
[Back to constructors index](/API_docs/constructors/index.html)



Used to [pay to upgrade a Gift to a collectible gift](https://core.telegram.org/api/gifts#upgrade-a-gift-to-a-collectible-gift), see the [collectible gifts »](https://core.telegram.org/api/gifts#collectible-gifts) documentation for more info on the full flow.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|keep\_original\_details|[Bool](/API_docs/types/Bool.html) | Optional|Set this flag to keep the original gift text, sender and receiver in the upgraded gift as a [starGiftAttributeOriginalDetails](../constructors/starGiftAttributeOriginalDetails.html) attribute.|
|stargift|[InputSavedStarGift](/API_docs/types/InputSavedStarGift.html) | Yes|The identifier of the received gift to upgrade.|



### Type: [InputInvoice](/API_docs/types/InputInvoice.html)


### Example:

```
$inputInvoiceStarGiftUpgrade = ['_' => 'inputInvoiceStarGiftUpgrade', 'keep_original_details' => Bool, 'stargift' => InputSavedStarGift];
```  
