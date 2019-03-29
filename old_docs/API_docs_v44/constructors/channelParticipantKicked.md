---
title: channelParticipantKicked
description: Channel participant kicked
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantKicked  
[Back to constructors index](index.md)



Channel participant kicked

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|kicked\_by|[int](../types/int.md) | Yes|Kicked by|
|date|[int](../types/int.md) | Yes|Date|



### Type: [ChannelParticipant](../types/ChannelParticipant.md)


### Example:

```php
$channelParticipantKicked = ['_' => 'channelParticipantKicked', 'user_id' => int, 'kicked_by' => int, 'date' => int];
```  


Or, if you're into Lua:

```lua
channelParticipantKicked={_='channelParticipantKicked', user_id=int, kicked_by=int, date=int}

```


