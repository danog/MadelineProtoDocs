---
title: "channelAdminLogEventActionEditMessage"
description: "A message was edited"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionEditMessage  
[Back to constructors index](/API_docs/constructors/index.html)



A message was edited

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_message|[Message](/API_docs/types/Message.html) | Optional|Old message|
|new\_message|[Message](/API_docs/types/Message.html) | Optional|New message|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionEditMessage = ['_' => 'channelAdminLogEventActionEditMessage', 'prev_message' => Message, 'new_message' => Message];
```  
