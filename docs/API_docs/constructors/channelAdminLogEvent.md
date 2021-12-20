---
title: "channelAdminLogEvent"
description: "Admin log event"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEvent  
[Back to constructors index](index.md)



Admin log event

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|Event ID|
|date|[int](../types/int.md) | Yes|Date|
|user\_id|[long](../types/long.md) | Yes|
|action|[ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md) | Yes|Action|



### Type: [ChannelAdminLogEvent](../types/ChannelAdminLogEvent.md)


### Example:

```php
$channelAdminLogEvent = ['_' => 'channelAdminLogEvent', 'id' => long, 'date' => int, 'user_id' => long, 'action' => ChannelAdminLogEventAction];
```  


Or, if you're into Lua:

```lua
channelAdminLogEvent={_='channelAdminLogEvent', id=long, date=int, user_id=long, action=ChannelAdminLogEventAction}

```


