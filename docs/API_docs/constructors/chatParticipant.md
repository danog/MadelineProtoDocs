---
title: "chatParticipant"
description: "Group member."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatParticipant  
[Back to constructors index](/API_docs/constructors/index.html)



Group member.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|Member user ID|
|inviter\_id|[long](/API_docs/types/long.html) | Yes|ID of the user that added the member to the group|
|date|[int](/API_docs/types/int.html) | Yes|Date added to the group|



### Type: [ChatParticipant](/API_docs/types/ChatParticipant.html)


### Example:

```
$chatParticipant = ['_' => 'chatParticipant', 'user_id' => long, 'inviter_id' => long, 'date' => int];
```  
