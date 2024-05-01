---
title: "messagePeerVoteInputOption"
description: "How a peer voted in a poll (reduced constructor, returned if an option was provided to messages.getPollVotes)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messagePeerVoteInputOption  
[Back to constructors index](/API_docs/constructors/index.html)



How a peer voted in a poll (reduced constructor, returned if an `option` was provided to [messages.getPollVotes](../methods/messages.getPollVotes.html))

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|The peer that voted for the queried `option`|
|date|[int](/API_docs/types/int.html) | Yes|When did the peer cast the vote|



### Type: [MessagePeerVote](/API_docs/types/MessagePeerVote.html)


### Example:

```
$messagePeerVoteInputOption = ['_' => 'messagePeerVoteInputOption', 'peer' => long, 'date' => int];
```  
