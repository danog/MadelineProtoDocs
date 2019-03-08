---
title: channelAdminLogEventActionStopPoll
description: Stopped poll
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionStopPoll  
[Back to constructors index](index.md)



Stopped poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](../types/Message.md) | Optional|Message|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionStopPoll = ['_' => 'channelAdminLogEventActionStopPoll', 'message' => Message];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "channelAdminLogEventActionStopPoll", "message": Message}
```


Or, if you're into Lua:

```lua
channelAdminLogEventActionStopPoll={_='channelAdminLogEventActionStopPoll', message=Message}

```


