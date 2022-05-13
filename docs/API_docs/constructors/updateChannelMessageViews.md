---
title: "updateChannelMessageViews"
description: "The view counter of a message in a channel has changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelMessageViews  
[Back to constructors index](/API_docs/constructors/index.html)



The view counter of a message in a channel has changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.html) | Yes|Channel ID|
|id|[int](/API_docs/types/int.html) | Yes|ID of the message|
|views|[int](/API_docs/types/int.html) | Yes|New view counter|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateChannelMessageViews = ['_' => 'updateChannelMessageViews', 'channel_id' => long, 'id' => int, 'views' => int];
```  
