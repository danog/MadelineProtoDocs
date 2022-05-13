---
title: "updateChatParticipant"
description: "A user has joined or left a specific chat"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatParticipant  
[Back to constructors index](/API_docs/constructors/index.html)



A user has joined or left a specific chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[long](/API_docs/types/long.html) | Yes|[Chat](https://core.telegram.org/api/channel) ID|
|date|[int](/API_docs/types/int.html) | Yes|When did this event occur|
|actor\_id|[long](/API_docs/types/long.html) | Yes|User that triggered the change (inviter, admin that kicked the user, or the even the **user\_id** itself)|
|user\_id|[long](/API_docs/types/long.html) | Yes|User that was affected by the change|
|prev\_participant|[ChatParticipant](/API_docs/types/ChatParticipant.html) | Optional|Previous participant info (empty if this participant just joined)|
|new\_participant|[ChatParticipant](/API_docs/types/ChatParticipant.html) | Optional|New participant info (empty if this participant just left)|
|invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Optional|The invite that was used to join the group|
|qts|[int](/API_docs/types/int.html) | Yes|New **qts** value, see [updates »](https://core.telegram.org/api/updates) for more info.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateChatParticipant = ['_' => 'updateChatParticipant', 'chat_id' => long, 'date' => int, 'actor_id' => long, 'user_id' => long, 'prev_participant' => ChatParticipant, 'new_participant' => ChatParticipant, 'invite' => ExportedChatInvite, 'qts' => int];
```  
