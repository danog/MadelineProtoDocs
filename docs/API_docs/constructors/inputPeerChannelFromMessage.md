---
title: "inputPeerChannelFromMessage"
description: "Defines a min channel that was seen in a certain message of a certain chat."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPeerChannelFromMessage  
[Back to constructors index](/API_docs/constructors/index.html)



Defines a [min](https://core.telegram.org/api/min) channel that was seen in a certain message of a certain chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|The chat where the channel's message was seen|
|msg\_id|[int](/API_docs/types/int.html) | Yes|The message ID|
|channel\_id|[long](/API_docs/types/long.html) | Yes|The identifier of the channel that was seen|



### Type: [InputPeer](/API_docs/types/InputPeer.html)


### Example:

```
$inputPeerChannelFromMessage = ['_' => 'inputPeerChannelFromMessage', 'peer' => InputPeer, 'msg_id' => int, 'channel_id' => long];
```  
