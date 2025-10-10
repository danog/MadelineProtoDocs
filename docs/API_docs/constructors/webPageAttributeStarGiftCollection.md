---
title: "webPageAttributeStarGiftCollection"
description: "Contains info about a gift collection » for a webPage preview of a gift collection » (the webPage will have a type of telegram_collection)."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webPageAttributeStarGiftCollection  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about a [gift collection »](https://core.telegram.org/api/gifts#gift-collections) for a [webPage](../constructors/webPage.html) preview of a [gift collection »](https://core.telegram.org/api/gifts#gift-collections) (the [webPage](../constructors/webPage.html) will have a `type` of `telegram_collection`).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|icons|Array of [Document](/API_docs/types/Document.html) | Yes|Gifts in the collection.|



### Type: [WebPageAttribute](/API_docs/types/WebPageAttribute.html)


### Example:

```
$webPageAttributeStarGiftCollection = ['_' => 'webPageAttributeStarGiftCollection', 'icons' => [Document, Document]];
```  
