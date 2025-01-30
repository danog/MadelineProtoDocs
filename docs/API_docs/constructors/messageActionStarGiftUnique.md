---
title: "messageActionStarGiftUnique"
description: "messageActionStarGiftUnique attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionStarGiftUnique  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|upgrade|[Bool](/API_docs/types/Bool.html) | Optional|
|transferred|[Bool](/API_docs/types/Bool.html) | Optional|
|saved|[Bool](/API_docs/types/Bool.html) | Optional|
|refunded|[Bool](/API_docs/types/Bool.html) | Optional|
|gift|[StarGift](/API_docs/types/StarGift.html) | Yes|
|can\_export\_at|[int](/API_docs/types/int.html) | Optional|
|transfer\_stars|[long](/API_docs/types/long.html) | Optional|
|from\_id|[Peer](/API_docs/types/Peer.html) | Optional|
|peer|[long](/API_docs/types/long.html) | Optional|
|saved\_id|[long](/API_docs/types/long.html) | Optional|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionStarGiftUnique = ['_' => 'messageActionStarGiftUnique', 'upgrade' => Bool, 'transferred' => Bool, 'saved' => Bool, 'refunded' => Bool, 'gift' => StarGift, 'can_export_at' => int, 'transfer_stars' => long, 'from_id' => Peer, 'peer' => long, 'saved_id' => long];
```  
