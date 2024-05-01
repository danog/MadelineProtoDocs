---
title: "messages.messageReactionsList"
description: "List of peers that reacted to a specific message"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_messageReactionsList.html
---
# Constructor: messages.messageReactionsList  
[Back to constructors index](/API_docs/constructors/index.html)



List of peers that reacted to a specific message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Total number of reactions matching query|
|reactions|Array of [MessagePeerReaction](/API_docs/types/MessagePeerReaction.html) | Yes|List of peers that reacted to a specific message|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Mentioned chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|
|next\_offset|[string](/API_docs/types/string.html) | Optional|If set, indicates the next offset to use to load more results by invoking [messages.getMessageReactionsList](../methods/messages.getMessageReactionsList.html).|



### Type: [messages.MessageReactionsList](/API_docs/types/messages.MessageReactionsList.html)


### Example:

```
$messages_messageReactionsList = ['_' => 'messages.messageReactionsList', 'count' => int, 'reactions' => [MessagePeerReaction, MessagePeerReaction], 'chats' => [Chat, Chat], 'users' => [User, User], 'next_offset' => 'string'];
```  
