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
|crafted|[Bool](/API_docs/types/Bool.html) | Optional|
|name|[string](/API_docs/types/string.html) | Yes|Name of the model|
|document|[Document](/API_docs/types/Document.html) | Optional|The [sticker](https://core.telegram.org/api/stickers) representing the upgraded gift|
|rarity|[StarGiftAttributeRarity](/API_docs/types/StarGiftAttributeRarity.html) | Yes|



### Type: [StarGiftAttribute](/API_docs/types/StarGiftAttribute.html)


### Example:

```
$starGiftAttributeModel = ['_' => 'starGiftAttributeModel', 'crafted' => Bool, 'name' => 'string', 'document' => Document, 'rarity' => StarGiftAttributeRarity];
```  
