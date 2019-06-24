---
title: channelAdminLogEventActionParticipantToggleAdmin
description: Admin toggled
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionParticipantToggleAdmin  
[Back to constructors index](index.md)



Admin toggled

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_participant|[ChannelParticipant](../types/ChannelParticipant.md) | Yes|Prev participant|
|new\_participant|[ChannelParticipant](../types/ChannelParticipant.md) | Yes|New participant|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionParticipantToggleAdmin = ['_' => 'channelAdminLogEventActionParticipantToggleAdmin', 'prev_participant' => ChannelParticipant, 'new_participant' => ChannelParticipant];
```  


Or, if you're into Lua:

```lua
channelAdminLogEventActionParticipantToggleAdmin={_='channelAdminLogEventActionParticipantToggleAdmin', prev_participant=ChannelParticipant, new_participant=ChannelParticipant}

```


