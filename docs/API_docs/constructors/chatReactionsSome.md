---
title: "chatReactionsSome"
description: "Some reactions are allowed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatReactionsSome  
[Back to constructors index](/API_docs/constructors/index.html)



Some reactions are allowed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|reactions|Array of [Reaction](/API_docs/types/Reaction.html) | Yes|Allowed set of reactions: the [reactions\_in\_chat\_max](https://core.telegram.org/api/config#reactions-in-chat-max) configuration field indicates the maximum number of reactions that can be specified in this field.|



### Type: [ChatReactions](/API_docs/types/ChatReactions.html)


### Example:

```
$chatReactionsSome = ['_' => 'chatReactionsSome', 'reactions' => [Reaction, Reaction]];
```  
