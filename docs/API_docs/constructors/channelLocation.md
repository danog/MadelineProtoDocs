---
title: "channelLocation"
description: "Geographical location of supergroup (geogroups)"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelLocation  
[Back to constructors index](index.md)



Geographical location of supergroup (geogroups)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo\_point|[GeoPoint](../types/GeoPoint.md) | Optional|Geographical location of supergrup|
|address|[string](../types/string.md) | Yes|Textual description of the address|



### Type: [ChannelLocation](../types/ChannelLocation.md)


### Example:

```php
$channelLocation = ['_' => 'channelLocation', 'geo_point' => GeoPoint, 'address' => 'string'];
```  


Or, if you're into Lua:

```lua
channelLocation={_='channelLocation', geo_point=GeoPoint, address='string'}

```


