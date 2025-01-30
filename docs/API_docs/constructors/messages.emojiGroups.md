---
title: "messages.emojiGroups"
description: "Represents a list of emoji categories."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_emojiGroups.html
---
# Constructor: messages.emojiGroups  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a list of [emoji categories](https://core.telegram.org/api/emoji-categories).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](/API_docs/types/int.html) | Yes|
|groups|Array of [EmojiGroup](/API_docs/types/EmojiGroup.html) | Yes|A list of [emoji categories](https://core.telegram.org/api/emoji-categories).|



### Type: [messages.EmojiGroups](/API_docs/types/messages.EmojiGroups.html)


### Example:

```
$messages_emojiGroups = ['_' => 'messages.emojiGroups', 'hash' => int, 'groups' => [EmojiGroup, EmojiGroup]];
```  
