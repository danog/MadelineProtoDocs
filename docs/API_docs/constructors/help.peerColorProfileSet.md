---
title: "help.peerColorProfileSet"
description: "help.peerColorProfileSet attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_peerColorProfileSet.html
---
# Constructor: help.peerColorProfileSet  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|palette\_colors|Array of [int](/API_docs/types/int.html) | Yes|
|bg\_colors|Array of [int](/API_docs/types/int.html) | Yes|
|story\_colors|Array of [int](/API_docs/types/int.html) | Yes|



### Type: [help.PeerColorSet](/API_docs/types/help.PeerColorSet.html)


### Example:

```
$help_peerColorProfileSet = ['_' => 'help.peerColorProfileSet', 'palette_colors' => [int, int], 'bg_colors' => [int, int], 'story_colors' => [int, int]];
```  
