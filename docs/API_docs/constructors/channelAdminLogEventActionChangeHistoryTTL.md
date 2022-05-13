---
title: "channelAdminLogEventActionChangeHistoryTTL"
description: "The Time-To-Live of messages in this chat was changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangeHistoryTTL  
[Back to constructors index](/API_docs/constructors/index.html)



The Time-To-Live of messages in this chat was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_value|[int](/API_docs/types/int.html) | Yes|Previous value|
|new\_value|[int](/API_docs/types/int.html) | Yes|New value|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionChangeHistoryTTL = ['_' => 'channelAdminLogEventActionChangeHistoryTTL', 'prev_value' => int, 'new_value' => int];
```  
