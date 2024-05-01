---
title: "help.peerColorProfileSet"
description: "Represents a color palette that can be used in profile pages »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_peerColorProfileSet.html
---
# Constructor: help.peerColorProfileSet  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [color palette that can be used in profile pages »](https://core.telegram.org/api/colors).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|palette\_colors|Array of [int](/API_docs/types/int.html) | Yes|A list of 1-2 colors in RGB format, shown in the color palette settings to describe the current palette.|
|bg\_colors|Array of [int](/API_docs/types/int.html) | Yes|A list of 1-2 colors in RGB format describing the colors used to generate the actual background used in the profile page.|
|story\_colors|Array of [int](/API_docs/types/int.html) | Yes|A list of 2 colors in RGB format describing the colors of the gradient used for the unread active story indicator around the profile photo.|



### Type: [help.PeerColorSet](/API_docs/types/help.PeerColorSet.html)


### Example:

```
$help_peerColorProfileSet = ['_' => 'help.peerColorProfileSet', 'palette_colors' => [int, int], 'bg_colors' => [int, int], 'story_colors' => [int, int]];
```  
