---
title: "starGiftUnique"
description: "starGiftUnique attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starGiftUnique  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[long](/API_docs/types/long.html) | Yes|
|title|[string](/API_docs/types/string.html) | Yes|
|num|[int](/API_docs/types/int.html) | Yes|
|owner\_id|[long](/API_docs/types/long.html) | Yes|
|attributes|Array of [StarGiftAttribute](/API_docs/types/StarGiftAttribute.html) | Yes|
|availability\_issued|[int](/API_docs/types/int.html) | Yes|
|availability\_total|[int](/API_docs/types/int.html) | Yes|



### Type: [StarGift](/API_docs/types/StarGift.html)


### Example:

```
$starGiftUnique = ['_' => 'starGiftUnique', 'id' => long, 'title' => 'string', 'num' => int, 'owner_id' => long, 'attributes' => [StarGiftAttribute, StarGiftAttribute], 'availability_issued' => int, 'availability_total' => int];
```  
