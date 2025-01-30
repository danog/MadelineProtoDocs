---
title: "emojiGroup"
description: "Represents an emoji category."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: emojiGroup  
[Back to constructors index](/API_docs/constructors/index.html)



Represents an [emoji category](https://core.telegram.org/api/emoji-categories).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](/API_docs/types/string.html) | Yes|Category name, i.e. "Animals", "Flags", "Faces" and so on...|
|icon\_emoji\_id|[long](/API_docs/types/long.html) | Yes|A single custom emoji used as preview for the category.|
|emoticons|Array of [string](/API_docs/types/string.html) | Yes|A list of UTF-8 emojis, matching the category.|



### Type: [EmojiGroup](/API_docs/types/EmojiGroup.html)


### Example:

```
$emojiGroup = ['_' => 'emojiGroup', 'title' => 'string', 'icon_emoji_id' => long, 'emoticons' => ['string', 'string']];
```  
