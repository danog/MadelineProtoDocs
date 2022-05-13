---
title: "updateChatUserTyping"
description: "The user is preparing a message in a group; typing, recording, uploading, etc. This update is valid for 6 seconds. If no further updates of this kind are received after 6 seconds, it should be considered that the user stopped doing whatever they were doing"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatUserTyping  
[Back to constructors index](/API_docs/constructors/index.html)



The user is preparing a message in a group; typing, recording, uploading, etc. This update is valid for 6 seconds. If no further updates of this kind are received after 6 seconds, it should be considered that the user stopped doing whatever they were doing

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[long](/API_docs/types/long.html) | Yes|Group id|
|from\_id|[Peer](/API_docs/types/Peer.html) | Yes|Peer that started typing (can be the chat itself, in case of anonymous admins).|
|action|[SendMessageAction](/API_docs/types/SendMessageAction.html) | Yes|Type of action<br>Parameter added in [Layer 17](https://core.telegram.org/api/layers#layer-17).|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateChatUserTyping = ['_' => 'updateChatUserTyping', 'chat_id' => long, 'from_id' => Peer, 'action' => SendMessageAction];
```  
