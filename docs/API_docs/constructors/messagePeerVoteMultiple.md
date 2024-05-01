---
title: "messagePeerVoteMultiple"
description: "How a peer voted in a multiple-choice poll"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messagePeerVoteMultiple  
[Back to constructors index](/API_docs/constructors/index.html)



How a peer voted in a multiple-choice poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|Peer ID|
|options|Array of [bytes](/API_docs/types/bytes.html) | Yes|Options chosen by the peer|
|date|[int](/API_docs/types/int.html) | Yes|When did the peer cast their votes|



### Type: [MessagePeerVote](/API_docs/types/MessagePeerVote.html)


### Example:

```
$messagePeerVoteMultiple = ['_' => 'messagePeerVoteMultiple', 'peer' => long, 'options' => ['bytes', 'bytes'], 'date' => int];
```  
