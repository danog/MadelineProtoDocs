---
title: "channelAdminLogEventActionChangeUsernames"
description: "The list of usernames associated with the channel was changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangeUsernames  
[Back to constructors index](/API_docs/constructors/index.html)



The list of usernames associated with the channel was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_value|Array of [string](/API_docs/types/string.html) | Yes|Previous set of usernames|
|new\_value|Array of [string](/API_docs/types/string.html) | Yes|New set of usernames|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionChangeUsernames = ['_' => 'channelAdminLogEventActionChangeUsernames', 'prev_value' => ['string', 'string'], 'new_value' => ['string', 'string']];
```  
