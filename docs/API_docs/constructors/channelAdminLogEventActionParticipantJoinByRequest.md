---
title: "channelAdminLogEventActionParticipantJoinByRequest"
description: "channelAdminLogEventActionParticipantJoinByRequest attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionParticipantJoinByRequest  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|invite|[ExportedChatInvite](../types/ExportedChatInvite.md) | Yes|
|approved\_by|[long](../types/long.md) | Yes|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionParticipantJoinByRequest = ['_' => 'channelAdminLogEventActionParticipantJoinByRequest', 'invite' => ExportedChatInvite, 'approved_by' => long];
```  
