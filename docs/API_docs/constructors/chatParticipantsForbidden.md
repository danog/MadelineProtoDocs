---
title: "chatParticipantsForbidden"
description: "Info on members is unavailable"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatParticipantsForbidden  
[Back to constructors index](/API_docs/constructors/index.md)



Info on members is unavailable

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[long](/API_docs/types/long.md) | Yes|
|self\_participant|[ChatParticipant](/API_docs/types/ChatParticipant.md) | Optional|Info about the group membership of the current user|



### Type: [ChatParticipants](/API_docs/types/ChatParticipants.md)


### Example:

```php
$chatParticipantsForbidden = ['_' => 'chatParticipantsForbidden', 'chat_id' => long, 'self_participant' => ChatParticipant];
```  
