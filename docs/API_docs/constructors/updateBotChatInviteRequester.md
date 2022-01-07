---
title: "updateBotChatInviteRequester"
description: "updateBotChatInviteRequester attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotChatInviteRequester  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Peer](/API_docs/types/Peer.md) | Yes|
|date|[int](/API_docs/types/int.md) | Yes|
|user\_id|[long](/API_docs/types/long.md) | Yes|
|about|[string](/API_docs/types/string.md) | Yes|
|invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.md) | Yes|
|qts|[int](/API_docs/types/int.md) | Yes|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateBotChatInviteRequester = ['_' => 'updateBotChatInviteRequester', 'peer' => Peer, 'date' => int, 'user_id' => long, 'about' => 'string', 'invite' => ExportedChatInvite, 'qts' => int];
```  
