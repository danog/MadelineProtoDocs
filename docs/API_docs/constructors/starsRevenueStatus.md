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
|current\_balance|[StarsAmount](/API_docs/types/StarsAmount.html) | Yes|
|available\_balance|[StarsAmount](/API_docs/types/StarsAmount.html) | Yes|
|overall\_revenue|[StarsAmount](/API_docs/types/StarsAmount.html) | Yes|
|next\_withdrawal\_at|[int](/API_docs/types/int.html) | Optional|



### Type: [StarsRevenueStatus](/API_docs/types/StarsRevenueStatus.html)


### Example:

```
$starsRevenueStatus = ['_' => 'starsRevenueStatus', 'withdrawal_enabled' => Bool, 'current_balance' => StarsAmount, 'available_balance' => StarsAmount, 'overall_revenue' => StarsAmount, 'next_withdrawal_at' => int];
```  
