---
title: "searchPostsFlood"
description: "searchPostsFlood attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: searchPostsFlood  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|query\_is\_free|[Bool](/API_docs/types/Bool.html) | Optional|
|total\_daily|[int](/API_docs/types/int.html) | Yes|
|remains|[int](/API_docs/types/int.html) | Yes|
|wait\_till|[int](/API_docs/types/int.html) | Optional|
|stars\_amount|[long](/API_docs/types/long.html) | Yes|



### Type: [SearchPostsFlood](/API_docs/types/SearchPostsFlood.html)


### Example:

```
$searchPostsFlood = ['_' => 'searchPostsFlood', 'query_is_free' => Bool, 'total_daily' => int, 'remains' => int, 'wait_till' => int, 'stars_amount' => long];
```  
