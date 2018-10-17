---
title: channelAdminLogEventActionDeleteMessage
description: channelAdminLogEventActionDeleteMessage attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionDeleteMessage  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|message|[Message](../types/Message.md) | Optional|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionDeleteMessage = ['_' => 'channelAdminLogEventActionDeleteMessage', 'message' => Message];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "channelAdminLogEventActionDeleteMessage", "message": Message}
```


Or, if you're into Lua:

```lua
channelAdminLogEventActionDeleteMessage={_='channelAdminLogEventActionDeleteMessage', message=Message}

```


