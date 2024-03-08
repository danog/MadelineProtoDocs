---
title: "messageActionGiveawayResults"
description: "A giveaway has ended."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGiveawayResults  
[Back to constructors index](/API_docs/constructors/index.html)



A [giveaway](https://core.telegram.org/api/giveaways) has ended.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|winners\_count|[int](/API_docs/types/int.html) | Yes|Number of winners in the giveaway|
|unclaimed\_count|[int](/API_docs/types/int.html) | Yes|Number of undistributed prizes|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionGiveawayResults = ['_' => 'messageActionGiveawayResults', 'winners_count' => int, 'unclaimed_count' => int];
```  
