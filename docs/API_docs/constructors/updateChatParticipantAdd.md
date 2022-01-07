---
title: "updateChatParticipantAdd"
description: "New group member."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatParticipantAdd  
[Back to constructors index](index.md)



New group member.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[long](../types/long.md) | Yes|
|user\_id|[long](../types/long.md) | Yes|
|inviter\_id|[long](../types/long.md) | Yes|
|date|[int](../types/int.md) | Yes|When was the participant added|
|version|[int](../types/int.md) | Yes|Chat version number|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChatParticipantAdd = ['_' => 'updateChatParticipantAdd', 'chat_id' => long, 'user_id' => long, 'inviter_id' => long, 'date' => int, 'version' => int];
```  
