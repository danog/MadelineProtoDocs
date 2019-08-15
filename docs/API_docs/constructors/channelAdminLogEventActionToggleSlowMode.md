---
title: channelAdminLogEventActionToggleSlowMode
description: Channel admin log event action toggle slow mode
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionToggleSlowMode  
[Back to constructors index](index.md)



Channel admin log event action toggle slow mode

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_value|[int](../types/int.md) | Yes|Prev value|
|new\_value|[int](../types/int.md) | Yes|New value|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionToggleSlowMode = ['_' => 'channelAdminLogEventActionToggleSlowMode', 'prev_value' => int, 'new_value' => int];
```  


Or, if you're into Lua:

```lua
channelAdminLogEventActionToggleSlowMode={_='channelAdminLogEventActionToggleSlowMode', prev_value=int, new_value=int}

```


