---
title: "stats.broadcastRevenueTransactions"
description: "Channel ad revenue transactions »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stats_broadcastRevenueTransactions.html
---
# Constructor: stats.broadcastRevenueTransactions  
[Back to constructors index](/API_docs/constructors/index.html)



[Channel ad revenue transactions »](https://core.telegram.org/api/revenue).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Total number of transactions.|
|transactions|Array of [BroadcastRevenueTransaction](/API_docs/types/BroadcastRevenueTransaction.html) | Yes|Transactions|



### Type: [stats.BroadcastRevenueTransactions](/API_docs/types/stats.BroadcastRevenueTransactions.html)


### Example:

```
$stats_broadcastRevenueTransactions = ['_' => 'stats.broadcastRevenueTransactions', 'count' => int, 'transactions' => [BroadcastRevenueTransaction, BroadcastRevenueTransaction]];
```  
