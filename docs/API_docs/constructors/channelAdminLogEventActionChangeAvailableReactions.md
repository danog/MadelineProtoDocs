---
title: "channelAdminLogEventActionChangeAvailableReactions"
description: "The set of allowed message reactions » for this channel has changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangeAvailableReactions  
[Back to constructors index](/API_docs/constructors/index.html)



The set of allowed [message reactions »](https://core.telegram.org/api/reactions) for this channel has changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_value|[ChatReactions](/API_docs/types/ChatReactions.html) | Yes|Previously allowed reaction emojis|
|new\_value|[ChatReactions](/API_docs/types/ChatReactions.html) | Yes|New allowed reaction emojis|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionChangeAvailableReactions = ['_' => 'channelAdminLogEventActionChangeAvailableReactions', 'prev_value' => ChatReactions, 'new_value' => ChatReactions];
```  
