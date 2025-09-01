---
title: "payments.uniqueStarGiftValueInfo"
description: "payments.uniqueStarGiftValueInfo attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_uniqueStarGiftValueInfo.html
---
# Constructor: payments.uniqueStarGiftValueInfo  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|last\_sale\_on\_fragment|[Bool](/API_docs/types/Bool.html) | Optional|
|value\_is\_average|[Bool](/API_docs/types/Bool.html) | Optional|
|currency|[string](/API_docs/types/string.html) | Yes|
|value|[long](/API_docs/types/long.html) | Yes|
|initial\_sale\_date|[int](/API_docs/types/int.html) | Yes|
|initial\_sale\_stars|[long](/API_docs/types/long.html) | Yes|
|initial\_sale\_price|[long](/API_docs/types/long.html) | Yes|
|last\_sale\_date|[int](/API_docs/types/int.html) | Optional|
|last\_sale\_price|[long](/API_docs/types/long.html) | Optional|
|floor\_price|[long](/API_docs/types/long.html) | Optional|
|average\_price|[long](/API_docs/types/long.html) | Optional|
|listed\_count|[int](/API_docs/types/int.html) | Optional|
|fragment\_listed\_count|[int](/API_docs/types/int.html) | Optional|
|fragment\_listed\_url|[string](/API_docs/types/string.html) | Optional|



### Type: [payments.UniqueStarGiftValueInfo](/API_docs/types/payments.UniqueStarGiftValueInfo.html)


### Example:

```
$payments_uniqueStarGiftValueInfo = ['_' => 'payments.uniqueStarGiftValueInfo', 'last_sale_on_fragment' => Bool, 'value_is_average' => Bool, 'currency' => 'string', 'value' => long, 'initial_sale_date' => int, 'initial_sale_stars' => long, 'initial_sale_price' => long, 'last_sale_date' => int, 'last_sale_price' => long, 'floor_price' => long, 'average_price' => long, 'listed_count' => int, 'fragment_listed_count' => int, 'fragment_listed_url' => 'string'];
```  
