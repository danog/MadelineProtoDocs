---
title: "updateChannelParticipant"
description: "A participant has left, joined, was banned or admined in a channel or supergroup."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelParticipant  
[Back to constructors index](/API_docs/constructors/index.html)



A participant has left, joined, was banned or admined in a [channel or supergroup](https://core.telegram.org/api/channel).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.html) | Yes|Channel ID|
|date|[int](/API_docs/types/int.html) | Yes|Date of the event|
|actor\_id|[long](/API_docs/types/long.html) | Yes|User that triggered the change (inviter, admin that kicked the user, or the even the **user\_id** itself)|
|user\_id|[long](/API_docs/types/long.html) | Yes|User that was affected by the change|
|prev\_participant|[ChannelParticipant](/API_docs/types/ChannelParticipant.html) | Optional|Previous participant status|
|new\_participant|[ChannelParticipant](/API_docs/types/ChannelParticipant.html) | Optional|New participant status|
|invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Optional|Chat invite used to join the [channel/supergroup](https://core.telegram.org/api/channel)|
|qts|[int](/API_docs/types/int.html) | Yes|New **qts** value, see [updates »](https://core.telegram.org/api/updates) for more info.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateChannelParticipant = ['_' => 'updateChannelParticipant', 'channel_id' => long, 'date' => int, 'actor_id' => long, 'user_id' => long, 'prev_participant' => ChannelParticipant, 'new_participant' => ChannelParticipant, 'invite' => ExportedChatInvite, 'qts' => int];
```  
