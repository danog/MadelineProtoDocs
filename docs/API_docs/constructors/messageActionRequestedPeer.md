---
title: "messageActionRequestedPeer"
description: "Contains info about a peer that the user shared with the bot after clicking on a keyboardButtonRequestPeer button."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionRequestedPeer  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about a peer that the user shared with the bot after clicking on a [keyboardButtonRequestPeer](../constructors/keyboardButtonRequestPeer.html) button.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|button\_id|[int](/API_docs/types/int.html) | Yes|`button_id` contained in the [keyboardButtonRequestPeer](../constructors/keyboardButtonRequestPeer.html)|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|The shared peer|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionRequestedPeer = ['_' => 'messageActionRequestedPeer', 'button_id' => int, 'peer' => Peer];
```  
