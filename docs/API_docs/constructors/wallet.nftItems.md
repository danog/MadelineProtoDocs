---
title: "wallet.nftItems"
description: "wallet.nftItems attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/wallet_nftItems.html
---
# Constructor: wallet.nftItems  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|items|Array of [wallet.NftItem](/API_docs/constructors/wallet.NftItem.html) | Yes|
|next\_offset|[string](/API_docs/types/string.html) | Optional|



### Type: [wallet.NftItems](/API_docs/types/wallet.NftItems.html)


### Example:

```
$wallet_nftItems = ['_' => 'wallet.nftItems', 'items' => [wallet.NftItem, wallet.NftItem], 'next_offset' => 'string'];
```  
