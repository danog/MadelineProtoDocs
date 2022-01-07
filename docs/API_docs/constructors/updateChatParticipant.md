---
title: "updateChatParticipant"
description: "updateChatParticipant attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatParticipant  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chat\_id|[long](/API_docs/types/long.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|
|actor\_id|[long](/API_docs/types/long.html) | Yes|
|user\_id|[long](/API_docs/types/long.html) | Yes|
|prev\_participant|[ChatParticipant](/API_docs/types/ChatParticipant.html) | Optional|
|new\_participant|[ChatParticipant](/API_docs/types/ChatParticipant.html) | Optional|
|invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Optional|
|qts|[int](/API_docs/types/int.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```php
$updateChatParticipant = ['_' => 'updateChatParticipant', 'chat_id' => long, 'date' => int, 'actor_id' => long, 'user_id' => long, 'prev_participant' => ChatParticipant, 'new_participant' => ChatParticipant, 'invite' => ExportedChatInvite, 'qts' => int];
```  
