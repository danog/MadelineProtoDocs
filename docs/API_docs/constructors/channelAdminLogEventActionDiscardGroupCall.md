---
title: "channelAdminLogEventActionDiscardGroupCall"
description: "A group call was terminated"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionDiscardGroupCall  
[Back to constructors index](/API_docs/constructors/index.html)



A group call was terminated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Yes|The group call that was terminated|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionDiscardGroupCall = ['_' => 'channelAdminLogEventActionDiscardGroupCall', 'call' => InputGroupCall];
```  
