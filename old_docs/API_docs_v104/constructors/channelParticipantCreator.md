---
title: channelParticipantCreator
description: Channel participant creator
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantCreator  
[Back to constructors index](index.md)



Channel participant creator

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|rank|[string](../types/string.md) | Optional||



### Type: [ChannelParticipant](../types/ChannelParticipant.md)


### Example:

```php
$channelParticipantCreator = ['_' => 'channelParticipantCreator', 'user_id' => int, 'rank' => 'string'];
```  


Or, if you're into Lua:

```lua
channelParticipantCreator={_='channelParticipantCreator', user_id=int, rank='string'}

```


