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
|my|[Bool](/API_docs/types/Bool.html) | Optional|Starting from layer 159, [messages.sendReaction](../methods/messages.sendReaction.html) will send reactions from the peer (user or channel) specified using [messages.saveDefaultSendAs](../methods/messages.saveDefaultSendAs.html). <br>If set, this flag indicates that this reaction was sent by us, even if the `peer` doesn't point to the current account.|
|peer\_id|[Peer](/API_docs/types/Peer.html) | Yes|Peer that reacted to the message|
|date|[int](/API_docs/types/int.html) | Yes|When was this reaction added|
|reaction|[Reaction](/API_docs/types/Reaction.html) | Optional|Reaction emoji|



### Type: [MessagePeerReaction](/API_docs/types/MessagePeerReaction.html)


### Example:

```
$messagePeerReaction = ['_' => 'messagePeerReaction', 'big' => Bool, 'unread' => Bool, 'my' => Bool, 'peer_id' => Peer, 'date' => int, 'reaction' => Reaction];
```  
