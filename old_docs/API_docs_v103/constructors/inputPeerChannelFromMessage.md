---
title: inputPeerChannelFromMessage
description: Channel from message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPeerChannelFromMessage  
[Back to constructors index](index.md)



Channel from message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|Peer|
|msg\_id|[int](../types/int.md) | Yes|Message ID|
|channel\_id|[int](../types/int.md) | Yes|Channel ID|



### Type: [InputPeer](../types/InputPeer.md)


### Example:

```php
$inputPeerChannelFromMessage = ['_' => 'inputPeerChannelFromMessage', 'peer' => InputPeer, 'msg_id' => int, 'channel_id' => int];
```  


Or, if you're into Lua:

```lua
inputPeerChannelFromMessage={_='inputPeerChannelFromMessage', peer=InputPeer, msg_id=int, channel_id=int}

```


