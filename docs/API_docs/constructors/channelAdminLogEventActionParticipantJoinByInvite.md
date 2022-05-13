---
title: "channelAdminLogEventActionParticipantJoinByInvite"
description: "A user joined the supergroup/channel using a specific invite link"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionParticipantJoinByInvite  
[Back to constructors index](/API_docs/constructors/index.html)



A user joined the [supergroup/channel](https://core.telegram.org/api/channel) using a specific invite link

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Yes|The invite link used to join the [supergroup/channel](https://core.telegram.org/api/channel)|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionParticipantJoinByInvite = ['_' => 'channelAdminLogEventActionParticipantJoinByInvite', 'invite' => ExportedChatInvite];
```  
