---
title: "inputInvoiceStarGiftPrepaidUpgrade"
description: "Separately prepay for the upgrade of a gift »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputInvoiceStarGiftPrepaidUpgrade  
[Back to constructors index](/API_docs/constructors/index.html)



[Separately prepay for the upgrade of a gift »](https://core.telegram.org/api/gifts#prepaying-for-someone-elses-upgrade).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|The peer that owns the gift.|
|hash|[string](/API_docs/types/string.html) | Yes|The upgrade hash from [messageActionStarGift](../constructors/messageActionStarGift.html).`prepaid_upgrade_hash` or [savedStarGift](../constructors/savedStarGift.html).`prepaid_upgrade_hash`.|



### Type: [InputInvoice](/API_docs/types/InputInvoice.html)


### Example:

```
$inputInvoiceStarGiftPrepaidUpgrade = ['_' => 'inputInvoiceStarGiftPrepaidUpgrade', 'peer' => InputPeer, 'hash' => 'string'];
```  
