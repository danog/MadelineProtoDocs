---
title: channelParticipant
description: Channel/supergroup participant
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipant  
[Back to constructors index](index.md)



Channel/supergroup participant

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](../types/long.md) | Yes|
|date|[int](../types/int.md) | Yes|Date joined|



### Type: [ChannelParticipant](../types/ChannelParticipant.md)


### Example:

```php
$channelParticipant = ['_' => 'channelParticipant', 'user_id' => long, 'date' => int];
```  


Or, if you're into Lua:

```lua
channelParticipant={_='channelParticipant', user_id=long, date=int}

```


