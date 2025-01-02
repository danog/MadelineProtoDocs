---
title: "userStarGift"
description: "userStarGift attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: userStarGift  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|name\_hidden|[Bool](/API_docs/types/Bool.html) | Optional|
|unsaved|[Bool](/API_docs/types/Bool.html) | Optional|
|refunded|[Bool](/API_docs/types/Bool.html) | Optional|
|can\_upgrade|[Bool](/API_docs/types/Bool.html) | Optional|
|from\_id|[long](/API_docs/types/long.html) | Optional|
|date|[int](/API_docs/types/int.html) | Yes|
|gift|[StarGift](/API_docs/types/StarGift.html) | Yes|
|message|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Optional|
|convert\_stars|[long](/API_docs/types/long.html) | Optional|
|upgrade\_stars|[long](/API_docs/types/long.html) | Optional|
|can\_export\_at|[int](/API_docs/types/int.html) | Optional|
|transfer\_stars|[long](/API_docs/types/long.html) | Optional|



### Type: [UserStarGift](/API_docs/types/UserStarGift.html)


### Example:

```
$userStarGift = ['_' => 'userStarGift', 'name_hidden' => Bool, 'unsaved' => Bool, 'refunded' => Bool, 'can_upgrade' => Bool, 'from_id' => long, 'date' => int, 'gift' => StarGift, 'message' => TextWithEntities, 'msg_id' => int, 'convert_stars' => long, 'upgrade_stars' => long, 'can_export_at' => int, 'transfer_stars' => long];
```  
