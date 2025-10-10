---
title: "peerColorCollectible"
description: "peerColorCollectible attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: peerColorCollectible  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|collectible\_id|[long](/API_docs/types/long.html) | Yes|
|gift\_emoji\_id|[long](/API_docs/types/long.html) | Yes|
|background\_emoji\_id|[long](/API_docs/types/long.html) | Yes|
|accent\_color|[int](/API_docs/types/int.html) | Yes|
|colors|Array of [int](/API_docs/types/int.html) | Yes|
|dark\_accent\_color|[int](/API_docs/types/int.html) | Optional|
|dark\_colors|Array of [int](/API_docs/types/int.html) | Optional|



### Type: [PeerColor](/API_docs/types/PeerColor.html)


### Example:

```
$peerColorCollectible = ['_' => 'peerColorCollectible', 'collectible_id' => long, 'gift_emoji_id' => long, 'background_emoji_id' => long, 'accent_color' => int, 'colors' => [int, int], 'dark_accent_color' => int, 'dark_colors' => [int, int]];
```  
