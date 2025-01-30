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
|reactions\_as\_tags|[Bool](/API_docs/types/Bool.html) | Optional|If set or if there are no reactions, all present and future reactions should be treated as [message tags, see here » for more info](https://core.telegram.org/api/saved-messages#tags).|
|results|Array of [ReactionCount](/API_docs/types/ReactionCount.html) | Yes|Reactions|
|recent\_reactions|Array of [MessagePeerReaction](/API_docs/types/MessagePeerReaction.html) | Optional|List of recent peers and their reactions|
|top\_reactors|Array of [MessageReactor](/API_docs/types/MessageReactor.html) | Optional|[Paid Telegram Star reactions leaderboard »](https://core.telegram.org/api/reactions#paid-reactions) for this message.|



### Type: [MessageReactions](/API_docs/types/MessageReactions.html)


### Example:

```
$messageReactions = ['_' => 'messageReactions', 'min' => Bool, 'can_see_list' => Bool, 'reactions_as_tags' => Bool, 'results' => [ReactionCount, ReactionCount], 'recent_reactions' => [MessagePeerReaction, MessagePeerReaction], 'top_reactors' => [MessageReactor, MessageReactor]];
```  
