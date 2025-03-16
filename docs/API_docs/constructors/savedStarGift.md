---
title: "savedStarGift"
description: "savedStarGift attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: savedStarGift  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|name\_hidden|[Bool](/API_docs/types/Bool.html) | Optional|
|unsaved|[Bool](/API_docs/types/Bool.html) | Optional|
|refunded|[Bool](/API_docs/types/Bool.html) | Optional|
|can\_upgrade|[Bool](/API_docs/types/Bool.html) | Optional|
|pinned\_to\_top|[Bool](/API_docs/types/Bool.html) | Optional|
|from\_id|[Peer](/API_docs/types/Peer.html) | Optional|
|date|[int](/API_docs/types/int.html) | Yes|
|gift|[StarGift](/API_docs/types/StarGift.html) | Yes|
|message|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Optional|
|saved\_id|[long](/API_docs/types/long.html) | Optional|
|convert\_stars|[long](/API_docs/types/long.html) | Optional|
|upgrade\_stars|[long](/API_docs/types/long.html) | Optional|
|can\_export\_at|[int](/API_docs/types/int.html) | Optional|
|transfer\_stars|[long](/API_docs/types/long.html) | Optional|



### Type: [SavedStarGift](/API_docs/types/SavedStarGift.html)


### Example:

```
$savedStarGift = ['_' => 'savedStarGift', 'name_hidden' => Bool, 'unsaved' => Bool, 'refunded' => Bool, 'can_upgrade' => Bool, 'pinned_to_top' => Bool, 'from_id' => Peer, 'date' => int, 'gift' => StarGift, 'message' => TextWithEntities, 'msg_id' => int, 'saved_id' => long, 'convert_stars' => long, 'upgrade_stars' => long, 'can_export_at' => int, 'transfer_stars' => long];
```  
