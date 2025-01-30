---
title: "messageActionStarGift"
description: "messageActionStarGift attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionStarGift  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|name\_hidden|[Bool](/API_docs/types/Bool.html) | Optional|
|saved|[Bool](/API_docs/types/Bool.html) | Optional|
|converted|[Bool](/API_docs/types/Bool.html) | Optional|
|upgraded|[Bool](/API_docs/types/Bool.html) | Optional|
|refunded|[Bool](/API_docs/types/Bool.html) | Optional|
|can\_upgrade|[Bool](/API_docs/types/Bool.html) | Optional|
|gift|[StarGift](/API_docs/types/StarGift.html) | Yes|
|message|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Optional|
|convert\_stars|[long](/API_docs/types/long.html) | Optional|
|upgrade\_msg\_id|[int](/API_docs/types/int.html) | Optional|
|upgrade\_stars|[long](/API_docs/types/long.html) | Optional|
|from\_id|[Peer](/API_docs/types/Peer.html) | Optional|
|peer|[long](/API_docs/types/long.html) | Optional|
|saved\_id|[long](/API_docs/types/long.html) | Optional|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionStarGift = ['_' => 'messageActionStarGift', 'name_hidden' => Bool, 'saved' => Bool, 'converted' => Bool, 'upgraded' => Bool, 'refunded' => Bool, 'can_upgrade' => Bool, 'gift' => StarGift, 'message' => TextWithEntities, 'convert_stars' => long, 'upgrade_msg_id' => int, 'upgrade_stars' => long, 'from_id' => Peer, 'peer' => long, 'saved_id' => long];
```  
