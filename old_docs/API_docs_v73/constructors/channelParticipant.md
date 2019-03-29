---
title: channelParticipant
description: Channel participant
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipant  
[Back to constructors index](index.md)



Channel participant

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|date|[int](../types/int.md) | Yes|Date|



### Type: [ChannelParticipant](../types/ChannelParticipant.md)


### Example:

```php
$channelParticipant = ['_' => 'channelParticipant', 'user_id' => int, 'date' => int];
```  


Or, if you're into Lua:

```lua
channelParticipant={_='channelParticipant', user_id=int, date=int}

```


