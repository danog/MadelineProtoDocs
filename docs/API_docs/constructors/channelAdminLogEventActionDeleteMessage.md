---
title: "channelAdminLogEventActionDeleteMessage"
description: "A message was deleted"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionDeleteMessage  
[Back to constructors index](index.md)



A message was deleted

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](../types/Message.md) | Optional|The message that was deleted|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionDeleteMessage = ['_' => 'channelAdminLogEventActionDeleteMessage', 'message' => Message];
```  


Or, if you're into Lua:

```lua
channelAdminLogEventActionDeleteMessage={_='channelAdminLogEventActionDeleteMessage', message=Message}

```


