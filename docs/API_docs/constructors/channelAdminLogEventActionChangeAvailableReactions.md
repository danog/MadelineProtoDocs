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
|prev\_value|Array of [string](/API_docs/types/string.html) | Yes|Previously allowed reaction emojis|
|new\_value|Array of [string](/API_docs/types/string.html) | Yes|New allowed reaction emojis|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionChangeAvailableReactions = ['_' => 'channelAdminLogEventActionChangeAvailableReactions', 'prev_value' => ['string', 'string'], 'new_value' => ['string', 'string']];
```  
