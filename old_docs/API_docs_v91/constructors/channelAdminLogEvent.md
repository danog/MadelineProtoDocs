---
title: channelAdminLogEvent
description: Channel admin log event
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEvent  
[Back to constructors index](index.md)



Channel admin log event

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|date|[int](../types/int.md) | Yes|Date|
|user\_id|[int](../types/int.md) | Yes|User ID|
|action|[ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md) | Yes|Action|



### Type: [ChannelAdminLogEvent](../types/ChannelAdminLogEvent.md)


### Example:

```php
$channelAdminLogEvent = ['_' => 'channelAdminLogEvent', 'id' => long, 'date' => int, 'user_id' => int, 'action' => ChannelAdminLogEventAction];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "channelAdminLogEvent", "id": long, "date": int, "user_id": int, "action": ChannelAdminLogEventAction}
```


Or, if you're into Lua:

```lua
channelAdminLogEvent={_='channelAdminLogEvent', id=long, date=int, user_id=int, action=ChannelAdminLogEventAction}

```


