---
title: "updates.channelDifferenceEmpty"
description: "There are no new updates"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/updates_channelDifferenceEmpty.html
---
# Constructor: updates.channelDifferenceEmpty  
[Back to constructors index](/API_docs/constructors/index.html)



There are no new updates

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|final|[Bool](/API_docs/types/Bool.html) | Optional|Whether there are more updates that must be fetched (always false)|
|pts|[int](/API_docs/types/int.html) | Yes|The latest [PTS](https://core.telegram.org/api/updates)|
|timeout|[int](/API_docs/types/int.html) | Optional|Clients are supposed to refetch the channel difference after timeout seconds have elapsed|



### Type: [updates.ChannelDifference](/API_docs/types/updates.ChannelDifference.html)


### Example:

```
$updates_channelDifferenceEmpty = ['_' => 'updates.channelDifferenceEmpty', 'final' => Bool, 'pts' => int, 'timeout' => int];
```  
