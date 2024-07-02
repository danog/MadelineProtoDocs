---
title: "payments.starsRevenueStats"
description: "payments.starsRevenueStats attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_starsRevenueStats.html
---
# Constructor: payments.starsRevenueStats  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|revenue\_graph|[StatsGraph](/API_docs/types/StatsGraph.html) | Yes|
|status|[StarsRevenueStatus](/API_docs/types/StarsRevenueStatus.html) | Yes|
|usd\_rate|[double](/API_docs/types/double.html) | Yes|



### Type: [payments.StarsRevenueStats](/API_docs/types/payments.StarsRevenueStats.html)


### Example:

```
$payments_starsRevenueStats = ['_' => 'payments.starsRevenueStats', 'revenue_graph' => StatsGraph, 'status' => StarsRevenueStatus, 'usd_rate' => double];
```  
