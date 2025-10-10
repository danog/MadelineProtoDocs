---
title: "webPageAttributeUniqueStarGift"
description: "Contains info about collectible gift » for a webPage preview of a collectible gift » (the webPage will have a type of telegram_nft)."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webPageAttributeUniqueStarGift  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about [collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts) for a [webPage](../constructors/webPage.html) preview of a [collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts) (the [webPage](../constructors/webPage.html) will have a `type` of `telegram_nft`).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|gift|[StarGift](/API_docs/types/StarGift.html) | Yes|The [starGiftUnique](../constructors/starGiftUnique.html) constructor.|



### Type: [WebPageAttribute](/API_docs/types/WebPageAttribute.html)


### Example:

```
$webPageAttributeUniqueStarGift = ['_' => 'webPageAttributeUniqueStarGift', 'gift' => StarGift];
```  
