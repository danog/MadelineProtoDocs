---
title: "updatePendingJoinRequests"
description: "updatePendingJoinRequests attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePendingJoinRequests  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|
|requests\_pending|[int](/API_docs/types/int.html) | Yes|
|recent\_requesters|Array of [long](/API_docs/types/long.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```php
$updatePendingJoinRequests = ['_' => 'updatePendingJoinRequests', 'peer' => Peer, 'requests_pending' => int, 'recent_requesters' => [long, long]];
```  
