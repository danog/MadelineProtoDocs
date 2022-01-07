---
title: "chatInvitePeek"
description: "A chat invitation that also allows peeking into the group to read messages without joining it."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatInvitePeek  
[Back to constructors index](/API_docs/constructors/index.md)



A chat invitation that also allows peeking into the group to read messages without joining it.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat|[Chat](/API_docs/types/Chat.md) | Optional|Chat information|
|expires|[int](/API_docs/types/int.md) | Yes|Read-only anonymous access to this group will be revoked at this date|



### Type: [ChatInvite](/API_docs/types/ChatInvite.md)


### Example:

```php
$chatInvitePeek = ['_' => 'chatInvitePeek', 'chat' => Chat, 'expires' => int];
```  
