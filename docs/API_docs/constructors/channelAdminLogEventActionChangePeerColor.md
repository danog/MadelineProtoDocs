---
title: "channelAdminLogEventActionChangePeerColor"
description: "The message accent color was changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangePeerColor  
[Back to constructors index](/API_docs/constructors/index.html)



The [message accent color](https://core.telegram.org/api/colors) was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_value|[PeerColor](/API_docs/types/PeerColor.html) | Yes|Previous accent palette|
|new\_value|[PeerColor](/API_docs/types/PeerColor.html) | Yes|New accent palette|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionChangePeerColor = ['_' => 'channelAdminLogEventActionChangePeerColor', 'prev_value' => PeerColor, 'new_value' => PeerColor];
```  
