---
title: "sponsoredMessage"
description: "sponsoredMessage attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: sponsoredMessage  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|from\_id|[Peer](/API_docs/types/Peer.html) | Optional|
|chat\_invite|[ChatInvite](/API_docs/types/ChatInvite.html) | Optional|
|chat\_invite\_hash|[string](/API_docs/types/string.html) | Optional|
|channel\_post|[int](/API_docs/types/int.html) | Optional|
|start\_param|[string](/API_docs/types/string.html) | Optional|
|message|[string](/API_docs/types/string.html) | Yes|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Optional|



### Type: [SponsoredMessage](/API_docs/types/SponsoredMessage.html)


### Example:

```php
$sponsoredMessage = ['_' => 'sponsoredMessage', 'from_id' => Peer, 'chat_invite' => ChatInvite, 'chat_invite_hash' => 'string', 'channel_post' => int, 'start_param' => 'string', 'message' => 'string', 'entities' => [MessageEntity, MessageEntity]];
```  
