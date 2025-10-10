---
title: "updateChannelReadMessagesContents"
description: "The specified channel/supergroup messages were read (emitted specifically for messages like voice messages or video, only once the media is watched and marked as read using channels.readMessageContents)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelReadMessagesContents  
[Back to constructors index](/API_docs/constructors/index.html)



The specified [channel/supergroup](https://core.telegram.org/api/channel) messages were read (emitted specifically for messages like voice messages or video, only once the media is watched and marked as read using [channels.readMessageContents](../methods/channels.readMessageContents.html))

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.html) | Yes|[Channel/supergroup](https://core.telegram.org/api/channel) ID|
|top\_msg\_id|[int](/API_docs/types/int.html) | Optional|[Forum topic ID](https://core.telegram.org/api/forum#forum-topics).|
|saved\_peer\_id|[Peer](/API_docs/types/Peer.html) | Optional|If set, the messages were read within the specified [monoforum topic »](https://core.telegram.org/api/monoforum).|
|messages|Array of [int](/API_docs/types/int.html) | Yes|IDs of messages that were read|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateChannelReadMessagesContents = ['_' => 'updateChannelReadMessagesContents', 'channel_id' => long, 'top_msg_id' => int, 'saved_peer_id' => Peer, 'messages' => [int, int]];
```  
