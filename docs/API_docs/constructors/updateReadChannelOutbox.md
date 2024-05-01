---
title: "updateReadChannelOutbox"
description: "Outgoing messages in a channel/supergroup were read"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadChannelOutbox  
[Back to constructors index](/API_docs/constructors/index.html)



Outgoing messages in a [channel/supergroup](https://core.telegram.org/api/channel) were read

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.html) | Yes|Channel/supergroup ID|
|max\_id|[int](/API_docs/types/int.html) | Yes|Position up to which all outgoing messages are read.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateReadChannelOutbox = ['_' => 'updateReadChannelOutbox', 'channel_id' => long, 'max_id' => int];
```  
