---
title: "starGiftAttributePattern"
description: "A sticker applied on the backdrop of a collectible gift » using a repeating pattern."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starGiftAttributePattern  
[Back to constructors index](/API_docs/constructors/index.html)



A [sticker](https://core.telegram.org/api/stickers) applied on the backdrop of a [collectible gift »](https://core.telegram.org/api/gifts) using a repeating pattern.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|name|[string](/API_docs/types/string.html) | Yes|Name of the symbol|
|document|[Document](/API_docs/types/Document.html) | Optional|The symbol|
|rarity\_permille|[int](/API_docs/types/int.html) | Yes|The number of upgraded gifts that receive this backdrop for each 1000 gifts upgraded.|



### Type: [StarGiftAttribute](/API_docs/types/StarGiftAttribute.html)


### Example:

```
$starGiftAttributePattern = ['_' => 'starGiftAttributePattern', 'name' => 'string', 'document' => Document, 'rarity_permille' => int];
```  
