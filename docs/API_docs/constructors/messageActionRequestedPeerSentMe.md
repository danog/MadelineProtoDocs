---
title: "messageActionRequestedPeerSentMe"
description: "Contains info about one or more peers that the a user shared with the me (the bot) after clicking on a keyboardButtonRequestPeer button (service message received by the bot)."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionRequestedPeerSentMe  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about one or more peers that the a user shared with the me (the bot) after clicking on a [keyboardButtonRequestPeer](../constructors/keyboardButtonRequestPeer.html) button (service message received by the bot).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|button\_id|[int](/API_docs/types/int.html) | Yes|`button_id` contained in the [keyboardButtonRequestPeer](../constructors/keyboardButtonRequestPeer.html)|
|peers|Array of [RequestedPeer](/API_docs/types/RequestedPeer.html) | Yes|Info about the shared peers.|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionRequestedPeerSentMe = ['_' => 'messageActionRequestedPeerSentMe', 'button_id' => int, 'peers' => [RequestedPeer, RequestedPeer]];
```  
