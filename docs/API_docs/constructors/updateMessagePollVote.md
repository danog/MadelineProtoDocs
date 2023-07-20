---
title: "updateMessagePollVote"
description: "A specific user has voted in a poll"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateMessagePollVote  
[Back to constructors index](/API_docs/constructors/index.html)



A specific user has voted in a poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|poll\_id|[long](/API_docs/types/long.html) | Yes|Poll ID|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|
|options|Array of [bytes](/API_docs/types/bytes.html) | Yes|Chosen option(s)|
|qts|[int](/API_docs/types/int.html) | Yes|New **qts** value, see [updates »](https://core.telegram.org/api/updates) for more info.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateMessagePollVote = ['_' => 'updateMessagePollVote', 'poll_id' => long, 'peer' => Peer, 'options' => ['bytes', 'bytes'], 'qts' => int];
```  
