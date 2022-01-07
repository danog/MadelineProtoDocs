---
title: "inputChannelFromMessage"
description: "Defines a min channel that was seen in a certain message of a certain chat."
nav_exclude: true
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
|channel\_id|[long](../types/long.md) | Yes|



### Type: [InputChannel](../types/InputChannel.md)


### Example:

```php
$inputChannelFromMessage = ['_' => 'inputChannelFromMessage', 'peer' => InputPeer, 'msg_id' => int, 'channel_id' => long];
```  
