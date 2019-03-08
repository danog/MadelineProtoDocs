---
title: channelAdminLogEventActionStopPoll
description: channelAdminLogEventActionStopPoll attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionStopPoll  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|message|[Message](../types/Message.md) | Optional|



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


