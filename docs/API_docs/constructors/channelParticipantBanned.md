---
title: "channelParticipantBanned"
description: "Banned/kicked user"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantBanned  
[Back to constructors index](/API_docs/constructors/index.html)



Banned/kicked user

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|left|[Bool](/API_docs/types/Bool.html) | Optional|Whether the user has left the group|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|The banned peer|
|kicked\_by|[long](/API_docs/types/long.html) | Yes|User was kicked by the specified admin|
|date|[int](/API_docs/types/int.html) | Yes|When did the user join the group|
|banned\_rights|[ChatBannedRights](/API_docs/types/ChatBannedRights.html) | Yes|Banned [rights](https://core.telegram.org/api/rights)|



### Type: [ChannelParticipant](/API_docs/types/ChannelParticipant.html)


### Example:

```
$channelParticipantBanned = ['_' => 'channelParticipantBanned', 'left' => Bool, 'peer' => Peer, 'kicked_by' => long, 'date' => int, 'banned_rights' => ChatBannedRights];
```  
