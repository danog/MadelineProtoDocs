---
title: "walletOnchainGiftActionOfferAccept"
description: "walletOnchainGiftActionOfferAccept attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: walletOnchainGiftActionOfferAccept  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|buyer|[Bool](/API_docs/types/Bool.html) | Optional|
|offer\_address|[string](/API_docs/types/string.html) | Yes|
|counterparty\_address|[string](/API_docs/types/string.html) | Yes|
|price|[long](/API_docs/types/long.html) | Yes|
|service\_fee|[long](/API_docs/types/long.html) | Yes|



### Type: [WalletOnchainGiftAction](/API_docs/types/WalletOnchainGiftAction.html)


### Example:

```
$walletOnchainGiftActionOfferAccept = ['_' => 'walletOnchainGiftActionOfferAccept', 'buyer' => Bool, 'offer_address' => 'string', 'counterparty_address' => 'string', 'price' => long, 'service_fee' => long];
```  
