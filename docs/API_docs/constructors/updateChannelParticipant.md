---
title: updateChannelParticipant
description: updateChannelParticipant attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelParticipant  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|channel\_id|[int](../types/int.md) | Yes|
|date|[int](../types/int.md) | Yes|
|user\_id|[int](../types/int.md) | Yes|
|prev\_participant|[ChannelParticipant](../types/ChannelParticipant.md) | Optional|
|new\_participant|[ChannelParticipant](../types/ChannelParticipant.md) | Optional|
|qts|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChannelParticipant = ['_' => 'updateChannelParticipant', 'channel_id' => int, 'date' => int, 'user_id' => int, 'prev_participant' => ChannelParticipant, 'new_participant' => ChannelParticipant, 'qts' => int];
```  


Or, if you're into Lua:

```lua
updateChannelParticipant={_='updateChannelParticipant', channel_id=int, date=int, user_id=int, prev_participant=ChannelParticipant, new_participant=ChannelParticipant, qts=int}

```


