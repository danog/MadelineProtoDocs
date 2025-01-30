---
title: "emojiGroupGreeting"
description: "Represents an emoji category, that should be moved to the top of the list when choosing a sticker for a business introduction"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: emojiGroupGreeting  
[Back to constructors index](/API_docs/constructors/index.html)



Represents an [emoji category](https://core.telegram.org/api/emoji-categories), that should be moved to the top of the list when choosing a sticker for a [business introduction](https://core.telegram.org/api/business#business-introduction)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](/API_docs/types/string.html) | Yes|Category name, i.e. "Animals", "Flags", "Faces" and so on...|
|icon\_emoji\_id|[long](/API_docs/types/long.html) | Yes|A single custom emoji used as preview for the category.|
|emoticons|Array of [string](/API_docs/types/string.html) | Yes|A list of UTF-8 emojis, matching the category.|



### Type: [EmojiGroup](/API_docs/types/EmojiGroup.html)


### Example:

```
$emojiGroupGreeting = ['_' => 'emojiGroupGreeting', 'title' => 'string', 'icon_emoji_id' => long, 'emoticons' => ['string', 'string']];
```  
