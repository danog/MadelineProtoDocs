---
title: channelAdminLogEventActionChangeLocation
description: Channel location changed
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangeLocation  
[Back to constructors index](index.md)



Channel location changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_value|[ChannelLocation](../types/ChannelLocation.md) | Optional|Previous value|
|new\_value|[ChannelLocation](../types/ChannelLocation.md) | Optional|New value|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionChangeLocation = ['_' => 'channelAdminLogEventActionChangeLocation', 'prev_value' => ChannelLocation, 'new_value' => ChannelLocation];
```  


Or, if you're into Lua:

```lua
channelAdminLogEventActionChangeLocation={_='channelAdminLogEventActionChangeLocation', prev_value=ChannelLocation, new_value=ChannelLocation}

```


