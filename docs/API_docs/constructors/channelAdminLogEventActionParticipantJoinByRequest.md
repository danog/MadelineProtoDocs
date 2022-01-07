---
title: "channelAdminLogEventActionParticipantJoinByRequest"
description: "channelAdminLogEventActionParticipantJoinByRequest attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionParticipantJoinByRequest  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.md) | Yes|
|approved\_by|[long](/API_docs/types/long.md) | Yes|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionParticipantJoinByRequest = ['_' => 'channelAdminLogEventActionParticipantJoinByRequest', 'invite' => ExportedChatInvite, 'approved_by' => long];
```  
