---
title: "updateChannelAvailableMessages"
description: "The history of a channel/supergroup was hidden."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelAvailableMessages  
[Back to constructors index](/API_docs/constructors/index.html)



The history of a [channel/supergroup](https://core.telegram.org/api/channel) was hidden.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.html) | Yes|Channel/supergroup ID|
|available\_min\_id|[int](/API_docs/types/int.html) | Yes|Identifier of a maximum unavailable message in a channel due to hidden history.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateChannelAvailableMessages = ['_' => 'updateChannelAvailableMessages', 'channel_id' => long, 'available_min_id' => int];
```  
