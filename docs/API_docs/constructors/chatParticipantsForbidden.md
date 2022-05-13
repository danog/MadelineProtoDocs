---
title: "chatParticipantsForbidden"
description: "Info on members is unavailable"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatParticipantsForbidden  
[Back to constructors index](/API_docs/constructors/index.html)



Info on members is unavailable

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[long](/API_docs/types/long.html) | Yes|Group ID|
|self\_participant|[ChatParticipant](/API_docs/types/ChatParticipant.html) | Optional|Info about the group membership of the current user|



### Type: [ChatParticipants](/API_docs/types/ChatParticipants.html)


### Example:

```
$chatParticipantsForbidden = ['_' => 'chatParticipantsForbidden', 'chat_id' => long, 'self_participant' => ChatParticipant];
```  
