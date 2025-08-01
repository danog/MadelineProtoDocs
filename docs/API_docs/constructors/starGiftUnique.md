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
|require\_premium|[Bool](/API_docs/types/Bool.html) | Optional|
|resale\_ton\_only|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[long](/API_docs/types/long.html) | Yes|
|title|[string](/API_docs/types/string.html) | Yes|
|slug|[string](/API_docs/types/string.html) | Yes|
|num|[int](/API_docs/types/int.html) | Yes|
|owner\_id|[Peer](/API_docs/types/Peer.html) | Optional|
|owner\_name|[string](/API_docs/types/string.html) | Optional|
|owner\_address|[string](/API_docs/types/string.html) | Optional|
|attributes|Array of [StarGiftAttribute](/API_docs/types/StarGiftAttribute.html) | Yes|
|availability\_issued|[int](/API_docs/types/int.html) | Yes|
|availability\_total|[int](/API_docs/types/int.html) | Yes|
|gift\_address|[string](/API_docs/types/string.html) | Optional|
|resell\_amount|Array of [StarsAmount](/API_docs/types/StarsAmount.html) | Optional|
|released\_by|[Peer](/API_docs/types/Peer.html) | Optional|



### Type: [StarGift](/API_docs/types/StarGift.html)


### Example:

```
$starGiftUnique = ['_' => 'starGiftUnique', 'require_premium' => Bool, 'resale_ton_only' => Bool, 'id' => long, 'title' => 'string', 'slug' => 'string', 'num' => int, 'owner_id' => Peer, 'owner_name' => 'string', 'owner_address' => 'string', 'attributes' => [StarGiftAttribute, StarGiftAttribute], 'availability_issued' => int, 'availability_total' => int, 'gift_address' => 'string', 'resell_amount' => [StarsAmount, StarsAmount], 'released_by' => Peer];
```  
