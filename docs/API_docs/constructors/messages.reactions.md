---
title: "messages.reactions"
description: "messages.reactions attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_reactions.html
---
# Constructor: messages.reactions  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[long](/API_docs/types/long.html) | Yes|
|reactions|Array of [Reaction](/API_docs/types/Reaction.html) | Yes|



### Type: [messages.Reactions](/API_docs/types/messages.Reactions.html)


### Example:

```
$messages_reactions = ['_' => 'messages.reactions', 'hash' => long, 'reactions' => [Reaction, Reaction]];
```  
