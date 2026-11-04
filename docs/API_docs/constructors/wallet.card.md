---
title: "wallet.card"
description: "wallet.card attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/wallet_card.html
---
# Constructor: wallet.card  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|stickers|Array of [wallet.CardSticker](/API_docs/constructors/wallet.CardSticker.html) | Optional|
|bg\_nft\_item|[wallet.NftItem](/API_docs/constructors/wallet.NftItem.html) | Optional|
|address|[string](/API_docs/types/string.html) | Yes|
|balance|[long](/API_docs/types/long.html) | Yes|



### Type: [wallet.Card](/API_docs/types/wallet.Card.html)


### Example:

```
$wallet_card = ['_' => 'wallet.card', 'stickers' => [wallet.CardSticker, wallet.CardSticker], 'bg_nft_item' => wallet.NftItem, 'address' => 'string', 'balance' => long];
```  
