---
title: "boost"
description: "boost attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: boost  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|gift|[Bool](/API_docs/types/Bool.html) | Optional|
|giveaway|[Bool](/API_docs/types/Bool.html) | Optional|
|unclaimed|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[string](/API_docs/types/string.html) | Yes|
|user\_id|[long](/API_docs/types/long.html) | Optional|
|giveaway\_msg\_id|[int](/API_docs/types/int.html) | Optional|
|date|[int](/API_docs/types/int.html) | Yes|
|expires|[int](/API_docs/types/int.html) | Yes|
|used\_gift\_slug|[string](/API_docs/types/string.html) | Optional|
|multiplier|[int](/API_docs/types/int.html) | Optional|



### Type: [Boost](/API_docs/types/Boost.html)


### Example:

```
$boost = ['_' => 'boost', 'gift' => Bool, 'giveaway' => Bool, 'unclaimed' => Bool, 'id' => 'string', 'user_id' => long, 'giveaway_msg_id' => int, 'date' => int, 'expires' => int, 'used_gift_slug' => 'string', 'multiplier' => int];
```  
