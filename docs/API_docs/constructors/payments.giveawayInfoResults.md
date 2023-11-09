---
title: "payments.giveawayInfoResults"
description: "payments.giveawayInfoResults attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_giveawayInfoResults.html
---
# Constructor: payments.giveawayInfoResults  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|winner|[Bool](/API_docs/types/Bool.html) | Optional|
|refunded|[Bool](/API_docs/types/Bool.html) | Optional|
|start\_date|[int](/API_docs/types/int.html) | Yes|
|gift\_code\_slug|[string](/API_docs/types/string.html) | Optional|
|finish\_date|[int](/API_docs/types/int.html) | Yes|
|winners\_count|[int](/API_docs/types/int.html) | Yes|
|activated\_count|[int](/API_docs/types/int.html) | Yes|



### Type: [payments.GiveawayInfo](/API_docs/types/payments.GiveawayInfo.html)


### Example:

```
$payments_giveawayInfoResults = ['_' => 'payments.giveawayInfoResults', 'winner' => Bool, 'refunded' => Bool, 'start_date' => int, 'gift_code_slug' => 'string', 'finish_date' => int, 'winners_count' => int, 'activated_count' => int];
```  
