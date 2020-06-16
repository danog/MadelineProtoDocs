---
title: channelAdminLogEventActionEditMessage
description: A message was edited
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionEditMessage  
[Back to constructors index](index.md)



A message was edited

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_message|[Message](../types/Message.md) | Optional|Old message|
|new\_message|[Message](../types/Message.md) | Optional|New message|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionEditMessage = ['_' => 'channelAdminLogEventActionEditMessage', 'prev_message' => Message, 'new_message' => Message];
```  


Or, if you're into Lua:

```lua
channelAdminLogEventActionEditMessage={_='channelAdminLogEventActionEditMessage', prev_message=Message, new_message=Message}

```


