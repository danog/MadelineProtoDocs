---
title: "channelAdminLogEventActionParticipantToggleAdmin"
description: "The admin rights of a user were changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionParticipantToggleAdmin  
[Back to constructors index](index.md)



The admin [rights](https://core.telegram.org/api/rights) of a user were changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_participant|[ChannelParticipant](../types/ChannelParticipant.md) | Yes|Previous admin rights|
|new\_participant|[ChannelParticipant](../types/ChannelParticipant.md) | Yes|New admin rights|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionParticipantToggleAdmin = ['_' => 'channelAdminLogEventActionParticipantToggleAdmin', 'prev_participant' => ChannelParticipant, 'new_participant' => ChannelParticipant];
```  
