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
|gift|[StarGift](/API_docs/types/StarGift.html) | Yes|
|message|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Optional|
|convert\_stars|[long](/API_docs/types/long.html) | Yes|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionStarGift = ['_' => 'messageActionStarGift', 'name_hidden' => Bool, 'saved' => Bool, 'converted' => Bool, 'gift' => StarGift, 'message' => TextWithEntities, 'convert_stars' => long];
```  
