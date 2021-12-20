---
title: "channelAdminLogEventActionChangeLocation"
description: "The geogroup location was changed"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangeLocation  
[Back to constructors index](index.md)



The geogroup location was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_value|[ChannelLocation](../types/ChannelLocation.md) | Optional|Previous location|
|new\_value|[ChannelLocation](../types/ChannelLocation.md) | Optional|New location|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionChangeLocation = ['_' => 'channelAdminLogEventActionChangeLocation', 'prev_value' => ChannelLocation, 'new_value' => ChannelLocation];
```  


Or, if you're into Lua:

```lua
channelAdminLogEventActionChangeLocation={_='channelAdminLogEventActionChangeLocation', prev_value=ChannelLocation, new_value=ChannelLocation}

```


