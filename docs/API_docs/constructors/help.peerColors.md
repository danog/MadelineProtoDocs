---
title: "help.peerColors"
description: "help.peerColors attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_peerColors.html
---
# Constructor: help.peerColors  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[int](/API_docs/types/int.html) | Yes|
|colors|Array of [help.PeerColorOption](/API_docs/constructors/help.PeerColorOption.html) | Yes|



### Type: [help.PeerColors](/API_docs/types/help.PeerColors.html)


### Example:

```
$help_peerColors = ['_' => 'help.peerColors', 'hash' => int, 'colors' => [help.PeerColorOption, help.PeerColorOption]];
```  
