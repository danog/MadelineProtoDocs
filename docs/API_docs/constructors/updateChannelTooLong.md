---
title: "updateChannelTooLong"
description: "There are new updates in the specified channel, the client must fetch them.  "
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelTooLong  
[Back to constructors index](/API_docs/constructors/index.html)



There are new updates in the specified channel, the client must fetch them.  
If the difference is too long or if the channel isn't currently in the states, start fetching from the specified pts.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.html) | Yes|The channel|
|pts|[int](/API_docs/types/int.html) | Optional|The [PTS](https://core.telegram.org/api/updates).|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateChannelTooLong = ['_' => 'updateChannelTooLong', 'channel_id' => long, 'pts' => int];
```  
