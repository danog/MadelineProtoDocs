---
title: "help.peerColorSet"
description: "Represents a color palette that can be used in message accents »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_peerColorSet.html
---
# Constructor: help.peerColorSet  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [color palette that can be used in message accents »](https://core.telegram.org/api/colors).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|colors|Array of [int](/API_docs/types/int.html) | Yes|A list of 1-3 colors in RGB format, describing the accent color.|



### Type: [help.PeerColorSet](/API_docs/types/help.PeerColorSet.html)


### Example:

```
$help_peerColorSet = ['_' => 'help.peerColorSet', 'colors' => [int, int]];
```  
