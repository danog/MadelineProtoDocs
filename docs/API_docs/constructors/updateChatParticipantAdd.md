---
title: "updateChatParticipantAdd"
description: "New group member."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatParticipantAdd  
[Back to constructors index](/API_docs/constructors/index.md)



New group member.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[long](/API_docs/types/long.md) | Yes|
|user\_id|[long](/API_docs/types/long.md) | Yes|
|inviter\_id|[long](/API_docs/types/long.md) | Yes|
|date|[int](/API_docs/types/int.md) | Yes|When was the participant added|
|version|[int](/API_docs/types/int.md) | Yes|Chat version number|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateChatParticipantAdd = ['_' => 'updateChatParticipantAdd', 'chat_id' => long, 'user_id' => long, 'inviter_id' => long, 'date' => int, 'version' => int];
```  
