---
title: "updateChannelReadMessagesContents"
description: "The specified channel/supergroup messages were read"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelReadMessagesContents  
[Back to constructors index](/API_docs/constructors/index.html)



The specified [channel/supergroup](https://core.telegram.org/api/channel) messages were read

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.html) | Yes|[Channel/supergroup](https://core.telegram.org/api/channel) ID|
|messages|Array of [int](/API_docs/types/int.html) | Yes|IDs of messages that were read|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateChannelReadMessagesContents = ['_' => 'updateChannelReadMessagesContents', 'channel_id' => long, 'messages' => [int, int]];
```  
