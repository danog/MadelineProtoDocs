---
title: "messages.availableReactions"
description: "Animations and metadata associated with message reactions »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_availableReactions.html
---
# Constructor: messages.availableReactions  
[Back to constructors index](/API_docs/constructors/index.html)



Animations and metadata associated with [message reactions »](https://core.telegram.org/api/reactions)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](/API_docs/types/int.html) | Yes|
|reactions|Array of [AvailableReaction](/API_docs/types/AvailableReaction.html) | Yes|Animations and metadata associated with [message reactions »](https://core.telegram.org/api/reactions)|



### Type: [messages.AvailableReactions](/API_docs/types/messages.AvailableReactions.html)


### Example:

```
$messages_availableReactions = ['_' => 'messages.availableReactions', 'hash' => int, 'reactions' => [AvailableReaction, AvailableReaction]];
```  
