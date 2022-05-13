---
title: "channelAdminLogEventActionParticipantJoinByRequest"
description: "A new member was accepted to the chat by an admin"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionParticipantJoinByRequest  
[Back to constructors index](/API_docs/constructors/index.html)



A new member was accepted to the chat by an admin

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Yes|The invite link that was used to join the chat|
|approved\_by|[long](/API_docs/types/long.html) | Yes|ID of the admin that approved the invite|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionParticipantJoinByRequest = ['_' => 'channelAdminLogEventActionParticipantJoinByRequest', 'invite' => ExportedChatInvite, 'approved_by' => long];
```  
