---
title: "updateChatDefaultBannedRights"
description: "Default banned rights in a normal chat were updated"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatDefaultBannedRights  
[Back to constructors index](/API_docs/constructors/index.html)



Default banned rights in a [normal chat](https://core.telegram.org/api/channel) were updated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|The chat|
|default\_banned\_rights|[ChatBannedRights](/API_docs/types/ChatBannedRights.html) | Yes|New default banned rights|
|version|[int](/API_docs/types/int.html) | Yes|Version|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateChatDefaultBannedRights = ['_' => 'updateChatDefaultBannedRights', 'peer' => Peer, 'default_banned_rights' => ChatBannedRights, 'version' => int];
```  
