---
title: "updateEditChannelMessage"
description: "A message was edited in a channel/supergroup"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateEditChannelMessage  
[Back to constructors index](/API_docs/constructors/index.html)



A message was edited in a [channel/supergroup](https://core.telegram.org/api/channel)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](/API_docs/types/Message.html) | Optional|The new message|
|pts|[int](/API_docs/types/int.html) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](/API_docs/types/int.html) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateEditChannelMessage = ['_' => 'updateEditChannelMessage', 'message' => Message, 'pts' => int, 'pts_count' => int];
```  
