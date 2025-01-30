---
title: "requestedPeerChannel"
description: "Info about a channel/supergroup, shared by a user with the currently logged in bot using messages.sendBotRequestedPeer."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: requestedPeerChannel  
[Back to constructors index](/API_docs/constructors/index.html)



Info about a [channel/supergroup](https://core.telegram.org/api/channel), shared by a user with the currently logged in bot using [messages.sendBotRequestedPeer](../methods/messages.sendBotRequestedPeer.html).

All fields except the ID are optional, and will be populated if present on the chosen channel/supergroup, according to the parameters of the requesting [inputKeyboardButtonRequestPeer](../constructors/inputKeyboardButtonRequestPeer.html).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.html) | Yes|Channel/supergroup ID.|
|title|[string](/API_docs/types/string.html) | Optional|Channel/supergroup title.|
|username|[string](/API_docs/types/string.html) | Optional|Channel/supergroup username.|
|photo|[Photo](/API_docs/types/Photo.html) | Optional|Channel/supergroup photo.|



### Type: [RequestedPeer](/API_docs/types/RequestedPeer.html)


### Example:

```
$requestedPeerChannel = ['_' => 'requestedPeerChannel', 'channel_id' => long, 'title' => 'string', 'username' => 'string', 'photo' => Photo];
```  
