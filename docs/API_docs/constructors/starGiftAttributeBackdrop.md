---
title: "starGiftAttributeBackdrop"
description: "The backdrop of a collectible gift »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starGiftAttributeBackdrop  
[Back to constructors index](/API_docs/constructors/index.html)



The backdrop of a [collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|name|[string](/API_docs/types/string.html) | Yes|Name of the backdrop|
|backdrop\_id|[int](/API_docs/types/int.html) | Yes|Unique ID of the backdrop|
|center\_color|[int](/API_docs/types/int.html) | Yes|Color of the center of the backdrop in RGB24 format.|
|edge\_color|[int](/API_docs/types/int.html) | Yes|Color of the edges of the backdrop in RGB24 format.|
|pattern\_color|[int](/API_docs/types/int.html) | Yes|Color of the [starGiftAttributePattern](../constructors/starGiftAttributePattern.html) applied on the backdrop in RGB24 format.|
|text\_color|[int](/API_docs/types/int.html) | Yes|Color of the text on the backdrop in RGB24 format.|
|rarity\_permille|[int](/API_docs/types/int.html) | Yes|The number of upgraded gifts that receive this backdrop for each 1000 gifts upgraded.|



### Type: [StarGiftAttribute](/API_docs/types/StarGiftAttribute.html)


### Example:

```
$starGiftAttributeBackdrop = ['_' => 'starGiftAttributeBackdrop', 'name' => 'string', 'backdrop_id' => int, 'center_color' => int, 'edge_color' => int, 'pattern_color' => int, 'text_color' => int, 'rarity_permille' => int];
```  
