---
title: "starsRevenueStatus"
description: "starsRevenueStatus attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starsRevenueStatus  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|withdrawal\_enabled|[Bool](/API_docs/types/Bool.html) | Optional|
|current\_balance|[long](/API_docs/types/long.html) | Yes|
|available\_balance|[long](/API_docs/types/long.html) | Yes|
|overall\_revenue|[long](/API_docs/types/long.html) | Yes|
|next\_withdrawal\_at|[int](/API_docs/types/int.html) | Optional|



### Type: [StarsRevenueStatus](/API_docs/types/StarsRevenueStatus.html)


### Example:

```
$starsRevenueStatus = ['_' => 'starsRevenueStatus', 'withdrawal_enabled' => Bool, 'current_balance' => long, 'available_balance' => long, 'overall_revenue' => long, 'next_withdrawal_at' => int];
```  
