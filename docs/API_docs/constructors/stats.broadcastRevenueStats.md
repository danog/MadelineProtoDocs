---
title: "stats.broadcastRevenueStats"
description: "Channel revenue ad statistics, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stats_broadcastRevenueStats.html
---
# Constructor: stats.broadcastRevenueStats  
[Back to constructors index](/API_docs/constructors/index.html)



[Channel revenue ad statistics, see here »](https://core.telegram.org/api/revenue) for more info.

Note that all balances and currency amounts and graph values are in the smallest unit of the chosen cryptocurrency (currently nanotons for TONs, so to obtain a value in USD divide the chosen amount by `10^9`, and then divide by `usd_rate`).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|top\_hours\_graph|[StatsGraph](/API_docs/types/StatsGraph.html) | Yes|Ad impressions graph|
|revenue\_graph|[StatsGraph](/API_docs/types/StatsGraph.html) | Yes|Ad revenue graph (in the smallest unit of the cryptocurrency in which revenue is calculated)|
|balances|[BroadcastRevenueBalances](/API_docs/types/BroadcastRevenueBalances.html) | Yes|Current balance, current withdrawable balance and overall revenue|
|usd\_rate|[double](/API_docs/types/double.html) | Yes|Current conversion rate of the cryptocurrency (**not** in the smallest unit) in which revenue is calculated to USD|



### Type: [stats.BroadcastRevenueStats](/API_docs/types/stats.BroadcastRevenueStats.html)


### Example:

```
$stats_broadcastRevenueStats = ['_' => 'stats.broadcastRevenueStats', 'top_hours_graph' => StatsGraph, 'revenue_graph' => StatsGraph, 'balances' => BroadcastRevenueBalances, 'usd_rate' => double];
```  
