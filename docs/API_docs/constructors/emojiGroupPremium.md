---
title: "emojiGroupPremium"
description: "An emoji category, used to select all Premium-only stickers (i.e. those with a Premium effect »)/Premium-only custom emojis (i.e. those where the documentAttributeCustomEmoji.free flag is not set)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: emojiGroupPremium  
[Back to constructors index](/API_docs/constructors/index.html)



An [emoji category](https://core.telegram.org/api/emoji-categories), used to select all [Premium](https://core.telegram.org/api/premium)-only stickers (i.e. those with a [Premium effect »](https://core.telegram.org/api/stickers#premium-animated-sticker-effects))/[Premium](https://core.telegram.org/api/premium)-only [custom emojis](https://core.telegram.org/api/custom-emoji) (i.e. those where the [documentAttributeCustomEmoji](../constructors/documentAttributeCustomEmoji.html).`free` flag is **not** set)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](/API_docs/types/string.html) | Yes|Category name, i.e. "Animals", "Flags", "Faces" and so on...|
|icon\_emoji\_id|[long](/API_docs/types/long.html) | Yes|A single custom emoji used as preview for the category.|



### Type: [EmojiGroup](/API_docs/types/EmojiGroup.html)


### Example:

```
$emojiGroupPremium = ['_' => 'emojiGroupPremium', 'title' => 'string', 'icon_emoji_id' => long];
```  
