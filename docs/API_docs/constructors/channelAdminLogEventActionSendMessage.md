---
title: "channelAdminLogEventActionSendMessage"
description: "A message was posted in a channel"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionSendMessage  
[Back to constructors index](/API_docs/constructors/index.html)



A message was posted in a channel

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](/API_docs/types/Message.html) | Optional|The message that was sent|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionSendMessage = ['_' => 'channelAdminLogEventActionSendMessage', 'message' => Message];
```  
