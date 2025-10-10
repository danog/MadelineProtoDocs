---
title: "searchPostsFlood"
description: "Indicates if the specified global post search » requires payment."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: searchPostsFlood  
[Back to constructors index](/API_docs/constructors/index.html)



Indicates if the specified [global post search »](https://core.telegram.org/api/search#posts-tab) requires payment.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_is\_free|[Bool](/API_docs/types/Bool.html) | Optional|The specified query is free (and it **will not use up free search slots**).|
|total\_daily|[int](/API_docs/types/int.html) | Yes|Total number of daily free search slots.|
|remains|[int](/API_docs/types/int.html) | Yes|Remaining number of free search slots.|
|wait\_till|[int](/API_docs/types/int.html) | Optional|If there are no more search slots, specifies the unixtime when more search slots will be available.|
|stars\_amount|[long](/API_docs/types/long.html) | Yes|The number of [Telegram Stars](https://core.telegram.org/api/stars) to pay for each non-free search.|



### Type: [SearchPostsFlood](/API_docs/types/SearchPostsFlood.html)


### Example:

```
$searchPostsFlood = ['_' => 'searchPostsFlood', 'query_is_free' => Bool, 'total_daily' => int, 'remains' => int, 'wait_till' => int, 'stars_amount' => long];
```  
