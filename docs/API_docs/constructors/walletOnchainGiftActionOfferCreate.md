---
title: "walletOnchainGiftActionOfferCreate"
description: "walletOnchainGiftActionOfferCreate attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: walletOnchainGiftActionOfferCreate  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|offer\_address|[string](/API_docs/types/string.html) | Yes|
|counterparty\_address|[string](/API_docs/types/string.html) | Optional|
|price|[long](/API_docs/types/long.html) | Yes|
|amount|[long](/API_docs/types/long.html) | Yes|
|service\_fee|[long](/API_docs/types/long.html) | Yes|
|expires\_at|[int](/API_docs/types/int.html) | Optional|



### Type: [WalletOnchainGiftAction](/API_docs/types/WalletOnchainGiftAction.html)


### Example:

```
$walletOnchainGiftActionOfferCreate = ['_' => 'walletOnchainGiftActionOfferCreate', 'offer_address' => 'string', 'counterparty_address' => 'string', 'price' => long, 'amount' => long, 'service_fee' => long, 'expires_at' => int];
```  
