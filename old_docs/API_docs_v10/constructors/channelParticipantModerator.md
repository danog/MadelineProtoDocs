---
title: channelParticipantModerator
description: channelParticipantModerator attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantModerator  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[int](../types/int.md) | Yes|
|inviter\_id|[int](../types/int.md) | Yes|
|date|[int](../types/int.md) | Yes|



### Type: [ChannelParticipant](../types/ChannelParticipant.md)


### Example:

```php
$channelParticipantModerator = ['_' => 'channelParticipantModerator', 'user_id' => int, 'inviter_id' => int, 'date' => int];
```  


Or, if you're into Lua:

```lua
channelParticipantModerator={_='channelParticipantModerator', user_id=int, inviter_id=int, date=int}

```


