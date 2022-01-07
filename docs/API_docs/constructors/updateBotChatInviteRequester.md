---
title: "updateBotChatInviteRequester"
description: "updateBotChatInviteRequester attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotChatInviteRequester  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Peer](../types/Peer.md) | Yes|
|date|[int](../types/int.md) | Yes|
|user\_id|[long](../types/long.md) | Yes|
|about|[string](../types/string.md) | Yes|
|invite|[ExportedChatInvite](../types/ExportedChatInvite.md) | Yes|
|qts|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateBotChatInviteRequester = ['_' => 'updateBotChatInviteRequester', 'peer' => Peer, 'date' => int, 'user_id' => long, 'about' => 'string', 'invite' => ExportedChatInvite, 'qts' => int];
```  
