---
title: "updateChannelParticipant"
description: "A participant has left, joined, was banned or admined in a channel or supergroup."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelParticipant  
[Back to constructors index](index.md)



A participant has left, joined, was banned or admined in a [channel or supergroup](https://core.telegram.org/api/channel).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](../types/long.md) | Yes|
|date|[int](../types/int.md) | Yes|Date of the event|
|actor\_id|[long](../types/long.md) | Yes|
|user\_id|[long](../types/long.md) | Yes|
|prev\_participant|[ChannelParticipant](../types/ChannelParticipant.md) | Optional|Previous participant status|
|new\_participant|[ChannelParticipant](../types/ChannelParticipant.md) | Optional|New participant status|
|invite|[ExportedChatInvite](../types/ExportedChatInvite.md) | Optional|
|qts|[int](../types/int.md) | Yes|[PTS](https://core.telegram.org/api/updates)|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChannelParticipant = ['_' => 'updateChannelParticipant', 'channel_id' => long, 'date' => int, 'actor_id' => long, 'user_id' => long, 'prev_participant' => ChannelParticipant, 'new_participant' => ChannelParticipant, 'invite' => ExportedChatInvite, 'qts' => int];
```  


Or, if you're into Lua:

```lua
updateChannelParticipant={_='updateChannelParticipant', channel_id=long, date=int, actor_id=long, user_id=long, prev_participant=ChannelParticipant, new_participant=ChannelParticipant, invite=ExportedChatInvite, qts=int}

```


