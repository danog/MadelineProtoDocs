---
title: "updateBotChatInviteRequester"
description: "Someone has requested to join a chat or channel (bots only, users will receive an updatePendingJoinRequests, instead)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotChatInviteRequester  
[Back to constructors index](/API_docs/constructors/index.html)



Someone has requested to join a chat or channel (bots only, users will receive an [updatePendingJoinRequests](../constructors/updatePendingJoinRequests.html), instead)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|The chat or channel in question|
|date|[int](/API_docs/types/int.html) | Yes|When was the [join request »](https://core.telegram.org/api/invites#join-requests) made|
|user\_id|[long](/API_docs/types/long.html) | Yes|The user ID that is asking to join the chat or channel|
|about|[string](/API_docs/types/string.html) | Yes|Bio of the user|
|invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Yes|Chat invite link that was used by the user to send the [join request »](https://core.telegram.org/api/invites#join-requests)|
|qts|[int](/API_docs/types/int.html) | Yes|[QTS](https://core.telegram.org/api/updates) event sequence identifier|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotChatInviteRequester = ['_' => 'updateBotChatInviteRequester', 'peer' => Peer, 'date' => int, 'user_id' => long, 'about' => 'string', 'invite' => ExportedChatInvite, 'qts' => int];
```  
