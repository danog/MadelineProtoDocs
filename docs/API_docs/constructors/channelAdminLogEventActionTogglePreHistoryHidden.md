---
title: "channelAdminLogEventActionTogglePreHistoryHidden"
description: "The hidden prehistory setting was changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionTogglePreHistoryHidden  
[Back to constructors index](index.md)



The hidden prehistory setting was [changed](../methods/channels.togglePreHistoryHidden.md)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|new\_value|[Bool](../types/Bool.md) | Yes|New value|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionTogglePreHistoryHidden = ['_' => 'channelAdminLogEventActionTogglePreHistoryHidden', 'new_value' => Bool];
```  


Or, if you're into Lua:

```lua
channelAdminLogEventActionTogglePreHistoryHidden={_='channelAdminLogEventActionTogglePreHistoryHidden', new_value=Bool}

```


