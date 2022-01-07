---
title: "updateChatParticipantDelete"
description: "A member has left the group."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatParticipantDelete  
[Back to constructors index](/API_docs/constructors/index.md)



A member has left the group.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[long](/API_docs/types/long.md) | Yes|
|user\_id|[long](/API_docs/types/long.md) | Yes|
|version|[int](/API_docs/types/int.md) | Yes|Used in basic groups to reorder updates and make sure that all of them was received.|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateChatParticipantDelete = ['_' => 'updateChatParticipantDelete', 'chat_id' => long, 'user_id' => long, 'version' => int];
```  
