---
title: "updateChannelMessageForwards"
description: "The forward counter of a message in a channel has changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelMessageForwards  
[Back to constructors index](/API_docs/constructors/index.html)



The forward counter of a message in a channel has changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.html) | Yes|Channel ID|
|id|[int](/API_docs/types/int.html) | Yes|ID of the message|
|forwards|[int](/API_docs/types/int.html) | Yes|New forward counter|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateChannelMessageForwards = ['_' => 'updateChannelMessageForwards', 'channel_id' => long, 'id' => int, 'forwards' => int];
```  
