---
title: "wallet.cardSticker"
description: "wallet.cardSticker attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/wallet_cardSticker.html
---
# Constructor: wallet.cardSticker  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|coordinates|[MediaAreaCoordinates](/API_docs/types/MediaAreaCoordinates.html) | Yes|
|nft|[wallet.NftItem](/API_docs/constructors/wallet.NftItem.html) | Yes|



### Type: [wallet.CardSticker](/API_docs/types/wallet.CardSticker.html)


### Example:

```
$wallet_cardSticker = ['_' => 'wallet.cardSticker', 'coordinates' => MediaAreaCoordinates, 'nft' => wallet.NftItem];
```  
