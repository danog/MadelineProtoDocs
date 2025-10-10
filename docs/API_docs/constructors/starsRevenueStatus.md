---
title: "starsRevenueStatus"
description: "Describes Telegram Star revenue balances »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starsRevenueStatus  
[Back to constructors index](/API_docs/constructors/index.html)



Describes [Telegram Star revenue balances »](https://core.telegram.org/api/stars).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|withdrawal\_enabled|[Bool](/API_docs/types/Bool.html) | Optional|If set, the user may [withdraw](https://core.telegram.org/api/stars#withdrawing-revenue) up to `available_balance` stars.|
|current\_balance|[StarsAmount](/API_docs/types/StarsAmount.html) | Yes|Amount of not-yet-withdrawn Telegram Stars.|
|available\_balance|[StarsAmount](/API_docs/types/StarsAmount.html) | Yes|Amount of withdrawable Telegram Stars.|
|overall\_revenue|[StarsAmount](/API_docs/types/StarsAmount.html) | Yes|Total amount of earned Telegram Stars.|
|next\_withdrawal\_at|[int](/API_docs/types/int.html) | Optional|Unixtime indicating when will withdrawal be available to the user. If not set, withdrawal can be started now.|



### Type: [StarsRevenueStatus](/API_docs/types/StarsRevenueStatus.html)


### Example:

```
$starsRevenueStatus = ['_' => 'starsRevenueStatus', 'withdrawal_enabled' => Bool, 'current_balance' => StarsAmount, 'available_balance' => StarsAmount, 'overall_revenue' => StarsAmount, 'next_withdrawal_at' => int];
```  
