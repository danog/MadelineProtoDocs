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
|user\_id|[long](../types/long.md) | Yes|
|inviter\_id|[long](../types/long.md) | Yes|
|date|[int](../types/int.md) | Yes|When did I join the channel/supergroup|



### Type: [ChannelParticipant](../types/ChannelParticipant.md)


### Example:

```php
$channelParticipantSelf = ['_' => 'channelParticipantSelf', 'user_id' => long, 'inviter_id' => long, 'date' => int];
```  


Or, if you're into Lua:

```lua
channelParticipantSelf={_='channelParticipantSelf', user_id=long, inviter_id=long, date=int}

```


