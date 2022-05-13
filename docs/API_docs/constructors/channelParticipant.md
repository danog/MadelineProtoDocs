---
title: "channelParticipant"
description: "Channel/supergroup participant"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipant  
[Back to constructors index](/API_docs/constructors/index.html)



Channel/supergroup participant

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|Participant user ID|
|date|[int](/API_docs/types/int.html) | Yes|Date joined|



### Type: [ChannelParticipant](/API_docs/types/ChannelParticipant.html)


### Example:

```
$channelParticipant = ['_' => 'channelParticipant', 'user_id' => long, 'date' => int];
```  
