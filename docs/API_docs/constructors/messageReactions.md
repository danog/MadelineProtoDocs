---
title: "messageReactions"
description: "Message reactions"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageReactions  
[Back to constructors index](/API_docs/constructors/index.md)



Message reactions

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|min|[Bool](/API_docs/types/Bool.md) | Optional|Similar to [min](https://core.telegram.org/api/min) objects, used for message reaction constructors that are the same for all users so they don't have the reactions sent by the current user (you can use [messages.getMessagesReactions](../methods/messages.getMessagesReactions.md) to get the full reaction info).|
|can\_see\_list|[Bool](/API_docs/types/Bool.md) | Optional|
|results|Array of [ReactionCount](/API_docs/types/ReactionCount.md) | Yes|Reactions|
|recent\_reactons|Array of [MessageUserReaction](/API_docs/types/MessageUserReaction.md) | Optional|



### Type: [MessageReactions](/API_docs/types/MessageReactions.md)


### Example:

```php
$messageReactions = ['_' => 'messageReactions', 'min' => Bool, 'can_see_list' => Bool, 'results' => [ReactionCount, ReactionCount], 'recent_reactons' => [MessageUserReaction, MessageUserReaction]];
```  
