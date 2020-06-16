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
|user\_id|[int](../types/int.md) | Yes|Pariticipant user ID|
|date|[int](../types/int.md) | Yes|Date joined|



### Type: [ChannelParticipant](../types/ChannelParticipant.md)


### Example:

```php
$channelParticipant = ['_' => 'channelParticipant', 'user_id' => int, 'date' => int];
```  


Or, if you're into Lua:

```lua
channelParticipant={_='channelParticipant', user_id=int, date=int}

```


