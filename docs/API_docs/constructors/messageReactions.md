---
title: "messageReactions"
description: "Message reactions »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageReactions  
[Back to constructors index](/API_docs/constructors/index.html)



[Message reactions »](https://core.telegram.org/api/reactions)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|min|[Bool](/API_docs/types/Bool.html) | Optional|Similar to [min](https://core.telegram.org/api/min) objects, used for [message reaction »](https://core.telegram.org/api/reactions) constructors that are the same for all users so they don't have the reactions sent by the current user (you can use [messages.getMessagesReactions](../methods/messages.getMessagesReactions.html) to get the full reaction info).|
|can\_see\_list|[Bool](/API_docs/types/Bool.html) | Optional|Whether [messages.getMessageReactionsList](../methods/messages.getMessageReactionsList.html) can be used to see how each specific peer reacted to the message|
|results|Array of [ReactionCount](/API_docs/types/ReactionCount.html) | Yes|Reactions|
|recent\_reactions|Array of [MessagePeerReaction](/API_docs/types/MessagePeerReaction.html) | Optional|List of recent peers and their reactions|



### Type: [MessageReactions](/API_docs/types/MessageReactions.html)


### Example:

```
$messageReactions = ['_' => 'messageReactions', 'min' => Bool, 'can_see_list' => Bool, 'results' => [ReactionCount, ReactionCount], 'recent_reactions' => [MessagePeerReaction, MessagePeerReaction]];
```  
