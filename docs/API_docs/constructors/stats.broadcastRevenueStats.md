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
|current\_balance|[long](/API_docs/types/long.html) | Yes|
|available\_balance|[long](/API_docs/types/long.html) | Yes|
|overall\_revenue|[long](/API_docs/types/long.html) | Yes|
|usd\_rate|[double](/API_docs/types/double.html) | Yes|



### Type: [stats.BroadcastRevenueStats](/API_docs/types/stats.BroadcastRevenueStats.html)


### Example:

```
$stats_broadcastRevenueStats = ['_' => 'stats.broadcastRevenueStats', 'top_hours_graph' => StatsGraph, 'revenue_graph' => StatsGraph, 'current_balance' => long, 'available_balance' => long, 'overall_revenue' => long, 'usd_rate' => double];
```  
