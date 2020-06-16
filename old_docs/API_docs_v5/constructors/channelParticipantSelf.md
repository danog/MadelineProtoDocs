---
title: channelParticipantSelf
description: Myself
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantSelf  
[Back to constructors index](index.md)



Myself

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|inviter\_id|[int](../types/int.md) | Yes|User that invited me to the channel/supergroup|
|date|[int](../types/int.md) | Yes|When did I join the channel/supergroup|



### Type: [ChannelParticipant](../types/ChannelParticipant.md)


### Example:

```php
$channelParticipantSelf = ['_' => 'channelParticipantSelf', 'user_id' => int, 'inviter_id' => int, 'date' => int];
```  


Or, if you're into Lua:

```lua
channelParticipantSelf={_='channelParticipantSelf', user_id=int, inviter_id=int, date=int}

```


