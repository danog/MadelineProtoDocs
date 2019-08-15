---
title: channelAdminLogEventActionEditMessage
description: Edit message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionEditMessage  
[Back to constructors index](index.md)



Edit message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_message|[Message](../types/Message.md) | Optional|Prev message|
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


