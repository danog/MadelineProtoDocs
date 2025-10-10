---
title: "emojiStatusCollectible"
description: "An owned collectible gift » as emoji status."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: emojiStatusCollectible  
[Back to constructors index](/API_docs/constructors/index.html)



An [owned collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts) as emoji status.

**Cannot** be passed to [account.updateEmojiStatus](../methods/account.updateEmojiStatus.html), must be converted to an [inputEmojiStatusCollectible](../constructors/inputEmojiStatusCollectible.html) first before passing it to that method.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|collectible\_id|[long](/API_docs/types/long.html) | Yes|ID of the collectible (from [starGiftUnique](../constructors/starGiftUnique.html).`id`).|
|document\_id|[long](/API_docs/types/long.html) | Yes|ID of the [custom emoji](https://core.telegram.org/api/custom-emoji) representing the status.|
|title|[string](/API_docs/types/string.html) | Yes|Name of the collectible.|
|slug|[string](/API_docs/types/string.html) | Yes|Unique identifier of the collectible that may be used to create a [collectible gift link »](https://core.telegram.org/api/links#collectible-gift-link) for the current collectible, or to fetch further info about the collectible using [payments.getUniqueStarGift](../methods/payments.getUniqueStarGift.html).|
|pattern\_document\_id|[long](/API_docs/types/long.html) | Yes|The ID of a pattern to apply on the profile's backdrop, correlated to the [starGiftAttributePattern](../constructors/starGiftAttributePattern.html) from the gift in `slug`.|
|center\_color|[int](/API_docs/types/int.html) | Yes|Color of the center of the profile backdrop in RGB24 format, from the gift's [starGiftAttributeBackdrop](../constructors/starGiftAttributeBackdrop.html).|
|edge\_color|[int](/API_docs/types/int.html) | Yes|Color of the edges of the profile backdrop in RGB24 format, from the gift's [starGiftAttributeBackdrop](../constructors/starGiftAttributeBackdrop.html).|
|pattern\_color|[int](/API_docs/types/int.html) | Yes|Color of the `pattern_document_id` applied on the profile backdrop in RGB24 format, from the gift's [starGiftAttributeBackdrop](../constructors/starGiftAttributeBackdrop.html).|
|text\_color|[int](/API_docs/types/int.html) | Yes|Color of text on the profile backdrop in RGB24 format, from the gift's [starGiftAttributeBackdrop](../constructors/starGiftAttributeBackdrop.html).|
|until|[int](/API_docs/types/int.html) | Optional|If set, the emoji status will be active until the specified unixtime.|



### Type: [EmojiStatus](/API_docs/types/EmojiStatus.html)


### Example:

```
$emojiStatusCollectible = ['_' => 'emojiStatusCollectible', 'collectible_id' => long, 'document_id' => long, 'title' => 'string', 'slug' => 'string', 'pattern_document_id' => long, 'center_color' => int, 'edge_color' => int, 'pattern_color' => int, 'text_color' => int, 'until' => int];
```  
