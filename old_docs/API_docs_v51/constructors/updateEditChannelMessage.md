---
title: updateEditChannelMessage
description: A message was edited in a [channel/supergroup](https://core.telegram.org/api/channel)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateEditChannelMessage  
[Back to constructors index](index.md)



A message was edited in a [channel/supergroup](https://core.telegram.org/api/channel)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](../types/Message.md) | Optional|The new message|
|pts|[int](../types/int.md) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](../types/int.md) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateEditChannelMessage = ['_' => 'updateEditChannelMessage', 'message' => Message, 'pts' => int, 'pts_count' => int];
```  


Or, if you're into Lua:

```lua
updateEditChannelMessage={_='updateEditChannelMessage', message=Message, pts=int, pts_count=int}

```


