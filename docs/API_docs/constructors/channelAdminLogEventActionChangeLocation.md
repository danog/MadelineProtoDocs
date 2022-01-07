---
title: "channelAdminLogEventActionChangeLocation"
description: "The geogroup location was changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangeLocation  
[Back to constructors index](/API_docs/constructors/index.md)



The geogroup location was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_value|[ChannelLocation](/API_docs/types/ChannelLocation.md) | Optional|Previous location|
|new\_value|[ChannelLocation](/API_docs/types/ChannelLocation.md) | Optional|New location|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionChangeLocation = ['_' => 'channelAdminLogEventActionChangeLocation', 'prev_value' => ChannelLocation, 'new_value' => ChannelLocation];
```  
