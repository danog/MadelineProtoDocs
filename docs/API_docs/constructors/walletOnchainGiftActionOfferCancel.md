---
title: "walletOnchainGiftActionOfferCancel"
description: "walletOnchainGiftActionOfferCancel attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: walletOnchainGiftActionOfferCancel  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|offer\_address|[string](/API_docs/types/string.html) | Yes|
|counterparty\_address|[string](/API_docs/types/string.html) | Optional|
|price|[long](/API_docs/types/long.html) | Optional|
|refund\_amount|[long](/API_docs/types/long.html) | Yes|
|fine|[long](/API_docs/types/long.html) | Optional|



### Type: [WalletOnchainGiftAction](/API_docs/types/WalletOnchainGiftAction.html)


### Example:

```
$walletOnchainGiftActionOfferCancel = ['_' => 'walletOnchainGiftActionOfferCancel', 'offer_address' => 'string', 'counterparty_address' => 'string', 'price' => long, 'refund_amount' => long, 'fine' => long];
```  
