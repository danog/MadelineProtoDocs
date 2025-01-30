---
title: "messageReactor"
description: "Info about a user in the paid Star reactions leaderboard for a message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageReactor  
[Back to constructors index](/API_docs/constructors/index.html)



Info about a user in the [paid Star reactions leaderboard](https://core.telegram.org/api/reactions#paid-reactions) for a message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|top|[Bool](/API_docs/types/Bool.html) | Optional|If set, the reactor is one of the most active reactors; may be unset if the reactor is the current user.|
|my|[Bool](/API_docs/types/Bool.html) | Optional|If set, this reactor is the current user.|
|anonymous|[Bool](/API_docs/types/Bool.html) | Optional|If set, the reactor is anonymous.|
|peer\_id|[Peer](/API_docs/types/Peer.html) | Optional|Identifier of the peer that reacted: may be unset for anonymous reactors different from the current user (i.e. if the current user sent an anonymous reaction `anonymous` will be set but this field will also be set).|
|count|[int](/API_docs/types/int.html) | Yes|The number of sent Telegram Stars.|



### Type: [MessageReactor](/API_docs/types/MessageReactor.html)


### Example:

```
$messageReactor = ['_' => 'messageReactor', 'top' => Bool, 'my' => Bool, 'anonymous' => Bool, 'peer_id' => Peer, 'count' => int];
```  
