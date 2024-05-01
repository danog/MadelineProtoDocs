---
title: "channelAdminLogEventActionChangeLinkedChat"
description: "The linked chat was changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangeLinkedChat  
[Back to constructors index](/API_docs/constructors/index.html)



The linked chat was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_value|[long](/API_docs/types/long.html) | Yes|Previous linked chat|
|new\_value|[long](/API_docs/types/long.html) | Yes|New linked chat|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionChangeLinkedChat = ['_' => 'channelAdminLogEventActionChangeLinkedChat', 'prev_value' => long, 'new_value' => long];
```  
