---
title: "stats.broadcastRevenueStats"
description: "stats.broadcastRevenueStats attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stats_broadcastRevenueStats.html
---
# Constructor: stats.broadcastRevenueStats  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|top\_hours\_graph|[StatsGraph](/API_docs/types/StatsGraph.html) | Yes|
|revenue\_graph|[StatsGraph](/API_docs/types/StatsGraph.html) | Yes|
|balances|[BroadcastRevenueBalances](/API_docs/types/BroadcastRevenueBalances.html) | Yes|
|usd\_rate|[double](/API_docs/types/double.html) | Yes|



### Type: [stats.BroadcastRevenueStats](/API_docs/types/stats.BroadcastRevenueStats.html)


### Example:

```
$stats_broadcastRevenueStats = ['_' => 'stats.broadcastRevenueStats', 'top_hours_graph' => StatsGraph, 'revenue_graph' => StatsGraph, 'balances' => BroadcastRevenueBalances, 'usd_rate' => double];
```  
