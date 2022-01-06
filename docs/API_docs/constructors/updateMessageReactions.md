---
title: "updateMessageReactions"
description: "New message reactions are available"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateMessageReactions  
[Back to constructors index](index.md)



New message reactions are available

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|msg\_id|[int](../types/int.md) | Yes|Message ID|
|reactions|[MessageReactions](../types/MessageReactions.md) | Yes|Reactions|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateMessageReactions = ['_' => 'updateMessageReactions', 'peer' => Peer, 'msg_id' => int, 'reactions' => MessageReactions];
```  


Or, if you're into Lua:

```lua
updateMessageReactions={_='updateMessageReactions', peer=Peer, msg_id=int, reactions=MessageReactions}

```


