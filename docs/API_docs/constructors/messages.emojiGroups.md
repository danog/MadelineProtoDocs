---
title: "messages.emojiGroups"
description: "messages.emojiGroups attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_emojiGroups.html
---
# Constructor: messages.emojiGroups  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[int](/API_docs/types/int.html) | Yes|
|groups|Array of [EmojiGroup](/API_docs/types/EmojiGroup.html) | Yes|



### Type: [messages.EmojiGroups](/API_docs/types/messages.EmojiGroups.html)


### Example:

```
$messages_emojiGroups = ['_' => 'messages.emojiGroups', 'hash' => int, 'groups' => [EmojiGroup, EmojiGroup]];
```  
