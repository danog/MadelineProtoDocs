---
title: messageReplyHeader
description: messageReplyHeader attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageReplyHeader  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|reply\_to\_msg\_id|[int](../types/int.md) | Yes|
|reply\_to\_peer\_id|[Peer](../types/Peer.md) | Optional|
|reply\_to\_top\_id|[int](../types/int.md) | Optional|



### Type: [MessageReplyHeader](../types/MessageReplyHeader.md)


### Example:

```php
$messageReplyHeader = ['_' => 'messageReplyHeader', 'reply_to_msg_id' => int, 'reply_to_peer_id' => Peer, 'reply_to_top_id' => int];
```  


Or, if you're into Lua:

```lua
messageReplyHeader={_='messageReplyHeader', reply_to_msg_id=int, reply_to_peer_id=Peer, reply_to_top_id=int}

```


