---
title: "starGiftCollection"
description: "starGiftCollection attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starGiftCollection  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|collection\_id|[int](/API_docs/types/int.html) | Yes|
|title|[string](/API_docs/types/string.html) | Yes|
|icon|[Document](/API_docs/types/Document.html) | Optional|
|gifts\_count|[int](/API_docs/types/int.html) | Yes|
|hash|[long](/API_docs/types/long.html) | Yes|



### Type: [StarGiftCollection](/API_docs/types/StarGiftCollection.html)


### Example:

```
$starGiftCollection = ['_' => 'starGiftCollection', 'collection_id' => int, 'title' => 'string', 'icon' => Document, 'gifts_count' => int, 'hash' => long];
```  
