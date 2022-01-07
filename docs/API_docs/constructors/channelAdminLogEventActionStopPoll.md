---
title: "channelAdminLogEventActionStopPoll"
description: "A poll was stopped"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionStopPoll  
[Back to constructors index](/API_docs/constructors/index.md)



A poll was stopped

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](/API_docs/types/Message.md) | Optional|The poll that was stopped|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionStopPoll = ['_' => 'channelAdminLogEventActionStopPoll', 'message' => Message];
```  
