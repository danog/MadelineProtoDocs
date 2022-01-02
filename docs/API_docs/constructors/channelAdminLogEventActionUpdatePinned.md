---
title: "channelAdminLogEventActionUpdatePinned"
description: "A message was pinned"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionUpdatePinned  
[Back to constructors index](index.md)



A message was pinned

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](../types/Message.md) | Optional|The message that was pinned|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionUpdatePinned = ['_' => 'channelAdminLogEventActionUpdatePinned', 'message' => Message];
```  


Or, if you're into Lua:

```lua
channelAdminLogEventActionUpdatePinned={_='channelAdminLogEventActionUpdatePinned', message=Message}

```


