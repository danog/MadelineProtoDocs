---
title: "channelAdminLogEventActionChangePeerColor"
description: "channelAdminLogEventActionChangePeerColor attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangePeerColor  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|prev\_value|[PeerColor](/API_docs/types/PeerColor.html) | Yes|
|new\_value|[PeerColor](/API_docs/types/PeerColor.html) | Yes|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionChangePeerColor = ['_' => 'channelAdminLogEventActionChangePeerColor', 'prev_value' => PeerColor, 'new_value' => PeerColor];
```  
