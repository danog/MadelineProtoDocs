---
title: "statsGroupTopPoster"
description: "Information about an active user in a supergroup"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: statsGroupTopPoster  
[Back to constructors index](/API_docs/constructors/index.html)



Information about an active user in a supergroup

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|User ID|
|messages|[int](/API_docs/types/int.html) | Yes|Number of messages for [statistics](https://core.telegram.org/api/stats) period in consideration|
|avg\_chars|[int](/API_docs/types/int.html) | Yes|Average number of characters per message|



### Type: [StatsGroupTopPoster](/API_docs/types/StatsGroupTopPoster.html)


### Example:

```
$statsGroupTopPoster = ['_' => 'statsGroupTopPoster', 'user_id' => long, 'messages' => int, 'avg_chars' => int];
```  
