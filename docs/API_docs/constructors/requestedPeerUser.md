---
title: "requestedPeerUser"
description: "Info about a user, shared by a user with the currently logged in bot using messages.sendBotRequestedPeer."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: requestedPeerUser  
[Back to constructors index](/API_docs/constructors/index.html)



Info about a user, shared by a user with the currently logged in bot using [messages.sendBotRequestedPeer](../methods/messages.sendBotRequestedPeer.html).

All fields except the ID are optional, and will be populated if present on the chosen user, according to the parameters of the requesting [inputKeyboardButtonRequestPeer](../constructors/inputKeyboardButtonRequestPeer.html).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|User ID.|
|first\_name|[string](/API_docs/types/string.html) | Optional|First name.|
|last\_name|[string](/API_docs/types/string.html) | Optional|Last name.|
|username|[string](/API_docs/types/string.html) | Optional|Username.|
|photo|[Photo](/API_docs/types/Photo.html) | Optional|Profile photo.|



### Type: [RequestedPeer](/API_docs/types/RequestedPeer.html)


### Example:

```
$requestedPeerUser = ['_' => 'requestedPeerUser', 'user_id' => long, 'first_name' => 'string', 'last_name' => 'string', 'username' => 'string', 'photo' => Photo];
```  
