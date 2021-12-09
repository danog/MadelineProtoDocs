---
title: inputPeerChannelFromMessage
description: Defines a [min](https://core.telegram.org/api/min) channel that was seen in a certain message of a certain chat.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPeerChannelFromMessage  
[Back to constructors index](index.md)



Defines a [min](https://core.telegram.org/api/min) channel that was seen in a certain message of a certain chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|The chat where the channel's message was seen|
|msg\_id|[int](../types/int.md) | Yes|The message ID|
|channel\_id|[long](../types/long.md) | Yes|



### Type: [InputPeer](../types/InputPeer.md)


### Example:

```php
$inputPeerChannelFromMessage = ['_' => 'inputPeerChannelFromMessage', 'peer' => InputPeer, 'msg_id' => int, 'channel_id' => long];
```  


Or, if you're into Lua:

```lua
inputPeerChannelFromMessage={_='inputPeerChannelFromMessage', peer=InputPeer, msg_id=int, channel_id=long}

```


