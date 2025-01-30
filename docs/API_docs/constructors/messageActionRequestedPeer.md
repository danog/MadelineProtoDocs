---
title: "messageActionRequestedPeer"
description: "Contains info about one or more peers that the we (the user) shared with the bot after clicking on a keyboardButtonRequestPeer button (service message sent by the user)."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionRequestedPeer  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about one or more peers that the we (the user) shared with the bot after clicking on a [keyboardButtonRequestPeer](../constructors/keyboardButtonRequestPeer.html) button (service message sent by the user).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|button\_id|[int](/API_docs/types/int.html) | Yes|`button_id` contained in the [keyboardButtonRequestPeer](../constructors/keyboardButtonRequestPeer.html)|
|peers|Array of [Peer](/API_docs/types/Peer.html) | Yes|The shared peers|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionRequestedPeer = ['_' => 'messageActionRequestedPeer', 'button_id' => int, 'peers' => [Peer, Peer]];
```  
