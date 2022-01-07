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
|channel\_id|[long](/API_docs/types/long.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|Date of the event|
|actor\_id|[long](/API_docs/types/long.html) | Yes|
|user\_id|[long](/API_docs/types/long.html) | Yes|
|prev\_participant|[ChannelParticipant](/API_docs/types/ChannelParticipant.html) | Optional|Previous participant status|
|new\_participant|[ChannelParticipant](/API_docs/types/ChannelParticipant.html) | Optional|New participant status|
|invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Optional|
|qts|[int](/API_docs/types/int.html) | Yes|[PTS](https://core.telegram.org/api/updates)|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```php
$updateChannelParticipant = ['_' => 'updateChannelParticipant', 'channel_id' => long, 'date' => int, 'actor_id' => long, 'user_id' => long, 'prev_participant' => ChannelParticipant, 'new_participant' => ChannelParticipant, 'invite' => ExportedChatInvite, 'qts' => int];
```  
