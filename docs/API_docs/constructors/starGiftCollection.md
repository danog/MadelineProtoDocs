---
title: "starGiftCollection"
description: "Represents a star gift collection »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starGiftCollection  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [star gift collection »](https://core.telegram.org/api/gifts#gift-collections).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|collection\_id|[int](/API_docs/types/int.html) | Yes|The ID of the collection.|
|title|[string](/API_docs/types/string.html) | Yes|Title of the collection.|
|icon|[Document](/API_docs/types/Document.html) | Optional|Optional icon for the collection, taken from the first gift in the collection.|
|gifts\_count|[int](/API_docs/types/int.html) | Yes|Number of gifts in the collection.|
|hash|[long](/API_docs/types/long.html) | Yes|Field to use **instead of `collection_id`** when generating the hash to pass to [payments.getStarGiftCollections](../methods/payments.getStarGiftCollections.html).|



### Type: [StarGiftCollection](/API_docs/types/StarGiftCollection.html)


### Example:

```
$starGiftCollection = ['_' => 'starGiftCollection', 'collection_id' => int, 'title' => 'string', 'icon' => Document, 'gifts_count' => int, 'hash' => long];
```  
