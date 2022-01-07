---
title: "channelAdminLogEventActionToggleSlowMode"
description: "Slow mode setting for supergroups was changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionToggleSlowMode  
[Back to constructors index](/API_docs/constructors/index.md)



[Slow mode setting for supergroups was changed](../methods/channels.toggleSlowMode.md)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_value|[int](/API_docs/types/int.md) | Yes|Previous slow mode value|
|new\_value|[int](/API_docs/types/int.md) | Yes|New slow mode value|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionToggleSlowMode = ['_' => 'channelAdminLogEventActionToggleSlowMode', 'prev_value' => int, 'new_value' => int];
```  
