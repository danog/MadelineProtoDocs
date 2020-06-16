---
title: channelParticipantKicked
description: channelParticipantKicked attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantKicked  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[int](../types/int.md) | Yes|
|kicked\_by|[int](../types/int.md) | Yes|
|date|[int](../types/int.md) | Yes|



### Type: [ChannelParticipant](../types/ChannelParticipant.md)


### Example:

```php
$channelParticipantKicked = ['_' => 'channelParticipantKicked', 'user_id' => int, 'kicked_by' => int, 'date' => int];
```  


Or, if you're into Lua:

```lua
channelParticipantKicked={_='channelParticipantKicked', user_id=int, kicked_by=int, date=int}

```


