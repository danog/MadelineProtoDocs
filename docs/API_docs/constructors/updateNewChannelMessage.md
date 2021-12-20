---
title: "updateNewChannelMessage"
description: "A new message was sent in a channel/supergroup"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNewChannelMessage  
[Back to constructors index](index.md)



A new message was sent in a [channel/supergroup](https://core.telegram.org/api/channel)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](../types/Message.md) | Optional|New message|
|pts|[int](../types/int.md) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](../types/int.md) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateNewChannelMessage = ['_' => 'updateNewChannelMessage', 'message' => Message, 'pts' => int, 'pts_count' => int];
```  


Or, if you're into Lua:

```lua
updateNewChannelMessage={_='updateNewChannelMessage', message=Message, pts=int, pts_count=int}

```


