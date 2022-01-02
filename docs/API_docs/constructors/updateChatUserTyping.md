---
title: "updateChatUserTyping"
description: "The user is preparing a message in a group; typing, recording, uploading, etc. This update is valid for 6 seconds. If no repeated update received after 6 seconds, it should be considered that the user stopped doing whatever he's been doing."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatUserTyping  
[Back to constructors index](index.md)



The user is preparing a message in a group; typing, recording, uploading, etc. This update is valid for 6 seconds. If no repeated update received after 6 seconds, it should be considered that the user stopped doing whatever he's been doing.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[long](../types/long.md) | Yes|
|from\_id|[Peer](../types/Peer.md) | Yes|
|action|[SendMessageAction](../types/SendMessageAction.md) | Yes|Type of action<br>Parameter added in [Layer 17](https://core.telegram.org/api/layers#layer-17).|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChatUserTyping = ['_' => 'updateChatUserTyping', 'chat_id' => long, 'from_id' => Peer, 'action' => SendMessageAction];
```  


Or, if you're into Lua:

```lua
updateChatUserTyping={_='updateChatUserTyping', chat_id=long, from_id=Peer, action=SendMessageAction}

```


