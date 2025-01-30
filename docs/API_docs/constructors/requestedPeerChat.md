---
title: "requestedPeerChat"
description: "Info about a chat, shared by a user with the currently logged in bot using messages.sendBotRequestedPeer."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: requestedPeerChat  
[Back to constructors index](/API_docs/constructors/index.html)



Info about a [chat](https://core.telegram.org/api/channel), shared by a user with the currently logged in bot using [messages.sendBotRequestedPeer](../methods/messages.sendBotRequestedPeer.html).

All fields except the ID are optional, and will be populated if present on the chosen chat, according to the parameters of the requesting [inputKeyboardButtonRequestPeer](../constructors/inputKeyboardButtonRequestPeer.html).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[long](/API_docs/types/long.html) | Yes|Chat ID.|
|title|[string](/API_docs/types/string.html) | Optional|Chat title.|
|photo|[Photo](/API_docs/types/Photo.html) | Optional|Chat photo.|



### Type: [RequestedPeer](/API_docs/types/RequestedPeer.html)


### Example:

```
$requestedPeerChat = ['_' => 'requestedPeerChat', 'chat_id' => long, 'title' => 'string', 'photo' => Photo];
```  
