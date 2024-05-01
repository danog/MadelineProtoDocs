---
title: "emojiGroupGreeting"
description: "emojiGroupGreeting attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: emojiGroupGreeting  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|title|[string](/API_docs/types/string.html) | Yes|
|icon\_emoji\_id|[long](/API_docs/types/long.html) | Yes|
|emoticons|Array of [string](/API_docs/types/string.html) | Yes|



### Type: [EmojiGroup](/API_docs/types/EmojiGroup.html)


### Example:

```
$emojiGroupGreeting = ['_' => 'emojiGroupGreeting', 'title' => 'string', 'icon_emoji_id' => long, 'emoticons' => ['string', 'string']];
```  
