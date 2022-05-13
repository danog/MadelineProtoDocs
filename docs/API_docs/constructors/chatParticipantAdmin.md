---
title: "chatParticipantAdmin"
description: "Chat admin"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatParticipantAdmin  
[Back to constructors index](/API_docs/constructors/index.html)



Chat admin

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|ID of a group member that is admin|
|inviter\_id|[long](/API_docs/types/long.html) | Yes|ID of the user that added the member to the group|
|date|[int](/API_docs/types/int.html) | Yes|Date when the user was added|



### Type: [ChatParticipant](/API_docs/types/ChatParticipant.html)


### Example:

```
$chatParticipantAdmin = ['_' => 'chatParticipantAdmin', 'user_id' => long, 'inviter_id' => long, 'date' => int];
```  
