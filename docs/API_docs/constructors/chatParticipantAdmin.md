---
title: "chatParticipantAdmin"
description: "Chat admin"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatParticipantAdmin  
[Back to constructors index](/API_docs/constructors/index.md)



Chat admin

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.md) | Yes|
|inviter\_id|[long](/API_docs/types/long.md) | Yes|
|date|[int](/API_docs/types/int.md) | Yes|Date when the user was added|



### Type: [ChatParticipant](/API_docs/types/ChatParticipant.md)


### Example:

```php
$chatParticipantAdmin = ['_' => 'chatParticipantAdmin', 'user_id' => long, 'inviter_id' => long, 'date' => int];
```  
