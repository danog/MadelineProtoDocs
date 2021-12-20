---
title: "channelAdminLogEventActionStopPoll"
description: "A poll was stopped"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionStopPoll  
[Back to constructors index](index.md)



A poll was stopped

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](../types/Message.md) | Optional|The poll that was stopped|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionStopPoll = ['_' => 'channelAdminLogEventActionStopPoll', 'message' => Message];
```  


Or, if you're into Lua:

```lua
channelAdminLogEventActionStopPoll={_='channelAdminLogEventActionStopPoll', message=Message}

```


