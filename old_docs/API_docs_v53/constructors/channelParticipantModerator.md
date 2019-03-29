---
title: channelParticipantModerator
description: Channel participant moderator
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantModerator  
[Back to constructors index](index.md)



Channel participant moderator

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|inviter\_id|[int](../types/int.md) | Yes|Inviter ID|
|date|[int](../types/int.md) | Yes|Date|



### Type: [ChannelParticipant](../types/ChannelParticipant.md)


### Example:

```php
$channelParticipantModerator = ['_' => 'channelParticipantModerator', 'user_id' => int, 'inviter_id' => int, 'date' => int];
```  


Or, if you're into Lua:

```lua
channelParticipantModerator={_='channelParticipantModerator', user_id=int, inviter_id=int, date=int}

```


