---
title: "messagePeerReaction"
description: "How a certain peer reacted to the message"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messagePeerReaction  
[Back to constructors index](/API_docs/constructors/index.html)



How a certain peer reacted to the message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|big|[Bool](/API_docs/types/Bool.html) | Optional|Whether the specified [message reaction »](https://core.telegram.org/api/reactions) should elicit a bigger and longer reaction|
|unread|[Bool](/API_docs/types/Bool.html) | Optional|Whether the reaction wasn't yet marked as read by the current user|
|peer\_id|[Peer](/API_docs/types/Peer.html) | Yes|Peer that reacted to the message|
|reaction|[string](/API_docs/types/string.html) | Yes|Reaction emoji|



### Type: [MessagePeerReaction](/API_docs/types/MessagePeerReaction.html)


### Example:

```
$messagePeerReaction = ['_' => 'messagePeerReaction', 'big' => Bool, 'unread' => Bool, 'peer_id' => Peer, 'reaction' => 'string'];
```  
