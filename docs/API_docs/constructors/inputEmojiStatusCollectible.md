---
title: "inputEmojiStatusCollectible"
description: "An owned collectible gift » as emoji status: can only be used in account.updateEmojiStatus, is never returned by the API."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputEmojiStatusCollectible  
[Back to constructors index](/API_docs/constructors/index.html)



An [owned collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts) as emoji status: can only be used in [account.updateEmojiStatus](../methods/account.updateEmojiStatus.html), is never returned by the API.

Note that once set, the status will be returned to users as a [emojiStatusCollectible](../constructors/emojiStatusCollectible.html) constructor, instead (which **cannot** be passed to [account.updateEmojiStatus](../methods/account.updateEmojiStatus.html), and must be converted to an [inputEmojiStatusCollectible](../constructors/inputEmojiStatusCollectible.html) first).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|collectible\_id|[long](/API_docs/types/long.html) | Yes|ID of the collectible (from [starGiftUnique](../constructors/starGiftUnique.html).`id`).|
|until|[int](/API_docs/types/int.html) | Optional|If set, the emoji status will be active until the specified unixtime.|



### Type: [EmojiStatus](/API_docs/types/EmojiStatus.html)


### Example:

```
$inputEmojiStatusCollectible = ['_' => 'inputEmojiStatusCollectible', 'collectible_id' => long, 'until' => int];
```  
