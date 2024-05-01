---
title: "channelParticipantSelf"
description: "Myself"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantSelf  
[Back to constructors index](/API_docs/constructors/index.html)



Myself

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|via\_request|[Bool](/API_docs/types/Bool.html) | Optional|Whether I joined upon specific approval of an admin|
|user\_id|[long](/API_docs/types/long.html) | Yes|User ID|
|inviter\_id|[long](/API_docs/types/long.html) | Yes|User that invited me to the channel/supergroup|
|date|[int](/API_docs/types/int.html) | Yes|When did I join the channel/supergroup|



### Type: [ChannelParticipant](/API_docs/types/ChannelParticipant.html)


### Example:

```
$channelParticipantSelf = ['_' => 'channelParticipantSelf', 'via_request' => Bool, 'user_id' => long, 'inviter_id' => long, 'date' => int];
```  
