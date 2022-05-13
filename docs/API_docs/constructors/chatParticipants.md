---
title: "chatParticipants"
description: "Group members."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatParticipants  
[Back to constructors index](/API_docs/constructors/index.html)



Group members.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[long](/API_docs/types/long.html) | Yes|Group identifier|
|participants|Array of [ChatParticipant](/API_docs/types/ChatParticipant.html) | Yes|List of group members|
|version|[int](/API_docs/types/int.html) | Yes|Group version number|



### Type: [ChatParticipants](/API_docs/types/ChatParticipants.html)


### Example:

```
$chatParticipants = ['_' => 'chatParticipants', 'chat_id' => long, 'participants' => [ChatParticipant, ChatParticipant], 'version' => int];
```  
