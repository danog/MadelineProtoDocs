---
title: "channelParticipantBanned"
description: "Banned/kicked user"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantBanned  
[Back to constructors index](/API_docs/constructors/index.md)



Banned/kicked user

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|left|[Bool](/API_docs/types/Bool.md) | Optional|Whether the user has left the group|
|peer|[Peer](/API_docs/types/Peer.md) | Yes|
|kicked\_by|[long](/API_docs/types/long.md) | Yes|
|date|[int](/API_docs/types/int.md) | Yes|When did the user join the group|
|banned\_rights|[ChatBannedRights](/API_docs/types/ChatBannedRights.md) | Yes|Banned [rights](https://core.telegram.org/api/rights)|



### Type: [ChannelParticipant](/API_docs/types/ChannelParticipant.md)


### Example:

```php
$channelParticipantBanned = ['_' => 'channelParticipantBanned', 'left' => Bool, 'peer' => Peer, 'kicked_by' => long, 'date' => int, 'banned_rights' => ChatBannedRights];
```  
