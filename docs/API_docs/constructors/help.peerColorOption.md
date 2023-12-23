---
title: "help.peerColorOption"
description: "help.peerColorOption attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_peerColorOption.html
---
# Constructor: help.peerColorOption  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hidden|[Bool](/API_docs/types/Bool.html) | Optional|
|color\_id|[int](/API_docs/types/int.html) | Yes|
|colors|[help.PeerColorSet](/API_docs/constructors/help.PeerColorSet.html) | Optional|
|dark\_colors|[help.PeerColorSet](/API_docs/constructors/help.PeerColorSet.html) | Optional|
|channel\_min\_level|[int](/API_docs/types/int.html) | Optional|



### Type: [help.PeerColorOption](/API_docs/types/help.PeerColorOption.html)


### Example:

```
$help_peerColorOption = ['_' => 'help.peerColorOption', 'hidden' => Bool, 'color_id' => int, 'colors' => help.PeerColorSet, 'dark_colors' => help.PeerColorSet, 'channel_min_level' => int];
```  
