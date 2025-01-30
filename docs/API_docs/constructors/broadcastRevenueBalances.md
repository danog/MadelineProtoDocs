---
title: "broadcastRevenueBalances"
description: "Describes channel ad revenue balances »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: broadcastRevenueBalances  
[Back to constructors index](/API_docs/constructors/index.html)



Describes [channel ad revenue balances »](https://core.telegram.org/api/revenue).

Note that all balances are in the smallest unit of the chosen cryptocurrency (currently nanotons for TONs, so to obtain a value in USD divide the chosen amount by `10^9`, and then divide by `usd_rate`).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|withdrawal\_enabled|[Bool](/API_docs/types/Bool.html) | Optional|If set, the available balance can be [withdrawn »](https://core.telegram.org/api/revenue#withdrawing-revenue).|
|current\_balance|[long](/API_docs/types/long.html) | Yes|Amount of not-yet-withdrawn cryptocurrency.|
|available\_balance|[long](/API_docs/types/long.html) | Yes|Amount of withdrawable cryptocurrency, out of the currently available balance (`available_balance <= current_balance`).|
|overall\_revenue|[long](/API_docs/types/long.html) | Yes|Total amount of earned cryptocurrency.|



### Type: [BroadcastRevenueBalances](/API_docs/types/BroadcastRevenueBalances.html)


### Example:

```
$broadcastRevenueBalances = ['_' => 'broadcastRevenueBalances', 'withdrawal_enabled' => Bool, 'current_balance' => long, 'available_balance' => long, 'overall_revenue' => long];
```  
