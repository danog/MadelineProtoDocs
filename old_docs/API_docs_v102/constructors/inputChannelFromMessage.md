---
title: inputChannelFromMessage
description: Defines a [min](https://core.telegram.org/api/min) channel that was seen in a certain message of a certain chat.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputChannelFromMessage  
[Back to constructors index](index.md)



Defines a [min](https://core.telegram.org/api/min) channel that was seen in a certain message of a certain chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|The chat where the channel was seen|
|msg\_id|[int](../types/int.md) | Yes|The message ID in the chat where the channel was seen|
|channel\_id|[int](../types/int.md) | Yes|The channel ID|



### Type: [InputChannel](../types/InputChannel.md)


### Example:

```php
$inputChannelFromMessage = ['_' => 'inputChannelFromMessage', 'peer' => InputPeer, 'msg_id' => int, 'channel_id' => int];
```  


Or, if you're into Lua:

```lua
inputChannelFromMessage={_='inputChannelFromMessage', peer=InputPeer, msg_id=int, channel_id=int}

```


