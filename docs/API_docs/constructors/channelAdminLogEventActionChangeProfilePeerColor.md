---
title: "channelAdminLogEventActionChangeProfilePeerColor"
description: "The profile accent color was changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangeProfilePeerColor  
[Back to constructors index](/API_docs/constructors/index.html)



The [profile accent color](https://core.telegram.org/api/colors) was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_value|[PeerColor](/API_docs/types/PeerColor.html) | Yes|Previous accent palette|
|new\_value|[PeerColor](/API_docs/types/PeerColor.html) | Yes|New accent palette|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionChangeProfilePeerColor = ['_' => 'channelAdminLogEventActionChangeProfilePeerColor', 'prev_value' => PeerColor, 'new_value' => PeerColor];
```  
