---
title: channelLocation
description: Physical location (getchats)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelLocation  
[Back to constructors index](index.md)



Physical location (getchats)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo\_point|[GeoPoint](../types/GeoPoint.md) | Optional|Geo point|
|address|[string](../types/string.md) | Yes|Physical address|



### Type: [ChannelLocation](../types/ChannelLocation.md)


### Example:

```php
$channelLocation = ['_' => 'channelLocation', 'geo_point' => GeoPoint, 'address' => 'string'];
```  


Or, if you're into Lua:

```lua
channelLocation={_='channelLocation', geo_point=GeoPoint, address='string'}

```


