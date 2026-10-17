---
title: "wallet.nftItem"
description: "wallet.nftItem attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/wallet_nftItem.html
---
# Constructor: wallet.nftItem  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|collection\_address|[string](/API_docs/types/string.html) | Optional|
|address|[string](/API_docs/types/string.html) | Yes|
|owner\_address|[string](/API_docs/types/string.html) | Yes|
|index|[string](/API_docs/types/string.html) | Yes|
|name|[string](/API_docs/types/string.html) | Optional|
|description|[string](/API_docs/types/string.html) | Optional|
|image|[WebDocument](/API_docs/types/WebDocument.html) | Optional|
|image\_small|[WebDocument](/API_docs/types/WebDocument.html) | Optional|
|content\_url|[WebDocument](/API_docs/types/WebDocument.html) | Optional|
|lottie|[WebDocument](/API_docs/types/WebDocument.html) | Optional|
|attributes|Array of [wallet.NftAttribute](/API_docs/constructors/wallet.NftAttribute.html) | Optional|
|extra|[DataJSON](/API_docs/types/DataJSON.html) | Optional|



### Type: [wallet.NftItem](/API_docs/types/wallet.NftItem.html)


### Example:

```
$wallet_nftItem = ['_' => 'wallet.nftItem', 'collection_address' => 'string', 'address' => 'string', 'owner_address' => 'string', 'index' => 'string', 'name' => 'string', 'description' => 'string', 'image' => WebDocument, 'image_small' => WebDocument, 'content_url' => WebDocument, 'lottie' => WebDocument, 'attributes' => [wallet.NftAttribute, wallet.NftAttribute], 'extra' => DataJSON];
```  
