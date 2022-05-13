---
title: "inputChannelFromMessage"
description: "Defines a min channel that was seen in a certain message of a certain chat."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputChannelFromMessage  
[Back to constructors index](/API_docs/constructors/index.html)



Defines a [min](https://core.telegram.org/api/min) channel that was seen in a certain message of a certain chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|The chat where the channel was seen|
|msg\_id|[int](/API_docs/types/int.html) | Yes|The message ID in the chat where the channel was seen|
|channel\_id|[long](/API_docs/types/long.html) | Yes|The channel ID|



### Type: [InputChannel](/API_docs/types/InputChannel.html)


### Example:

```
$inputChannelFromMessage = ['_' => 'inputChannelFromMessage', 'peer' => InputPeer, 'msg_id' => int, 'channel_id' => long];
```  
