---
title: "updateBotChatInviteRequester"
description: "updateBotChatInviteRequester attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotChatInviteRequester  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|
|user\_id|[long](/API_docs/types/long.html) | Yes|
|about|[string](/API_docs/types/string.html) | Yes|
|invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Yes|
|qts|[int](/API_docs/types/int.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```php
$updateBotChatInviteRequester = ['_' => 'updateBotChatInviteRequester', 'peer' => Peer, 'date' => int, 'user_id' => long, 'about' => 'string', 'invite' => ExportedChatInvite, 'qts' => int];
```  
