---
title: "stats.broadcastRevenueTransactions"
description: "stats.broadcastRevenueTransactions attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stats_broadcastRevenueTransactions.html
---
# Constructor: stats.broadcastRevenueTransactions  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.html) | Yes|
|transactions|Array of [BroadcastRevenueTransaction](/API_docs/types/BroadcastRevenueTransaction.html) | Yes|



### Type: [stats.BroadcastRevenueTransactions](/API_docs/types/stats.BroadcastRevenueTransactions.html)


### Example:

```
$stats_broadcastRevenueTransactions = ['_' => 'stats.broadcastRevenueTransactions', 'count' => int, 'transactions' => [BroadcastRevenueTransaction, BroadcastRevenueTransaction]];
```  
