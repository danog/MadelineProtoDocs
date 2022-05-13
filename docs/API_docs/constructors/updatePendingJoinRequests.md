---
title: "updatePendingJoinRequests"
description: "Someone has requested to join a chat or channel"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePendingJoinRequests  
[Back to constructors index](/API_docs/constructors/index.html)



Someone has requested to join a chat or channel

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|Chat or channel|
|requests\_pending|[int](/API_docs/types/int.html) | Yes|Number of pending [join requests »](https://core.telegram.org/api/invites#join-requests) for the chat or channel|
|recent\_requesters|Array of [long](/API_docs/types/long.html) | Yes|IDs of users that have recently requested to join|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updatePendingJoinRequests = ['_' => 'updatePendingJoinRequests', 'peer' => Peer, 'requests_pending' => int, 'recent_requesters' => [long, long]];
```  
