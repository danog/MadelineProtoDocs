---
title: "starGiftAttributeModel"
description: "The model of a collectible gift »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starGiftAttributeModel  
[Back to constructors index](/API_docs/constructors/index.html)



The model of a [collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|name|[string](/API_docs/types/string.html) | Yes|Name of the model|
|document|[Document](/API_docs/types/Document.html) | Optional|The [sticker](https://core.telegram.org/api/stickers) representing the upgraded gift|
|rarity\_permille|[int](/API_docs/types/int.html) | Yes|The number of upgraded gifts that receive this backdrop for each 1000 gifts upgraded.|



### Type: [StarGiftAttribute](/API_docs/types/StarGiftAttribute.html)


### Example:

```
$starGiftAttributeModel = ['_' => 'starGiftAttributeModel', 'name' => 'string', 'document' => Document, 'rarity_permille' => int];
```  
