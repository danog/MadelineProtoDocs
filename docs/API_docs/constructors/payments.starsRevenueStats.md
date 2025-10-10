---
title: "payments.starsRevenueStats"
description: "Star revenue statistics, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_starsRevenueStats.html
---
# Constructor: payments.starsRevenueStats  
[Back to constructors index](/API_docs/constructors/index.html)



[Star revenue statistics, see here »](https://core.telegram.org/api/stars) for more info.

Note that all balances and currency amounts and graph values are in Stars.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|top\_hours\_graph|[StatsGraph](/API_docs/types/StatsGraph.html) | Optional|For ad revenue statistics, ad impressions graph|
|revenue\_graph|[StatsGraph](/API_docs/types/StatsGraph.html) | Yes|Star revenue graph (number of earned stars)|
|status|[StarsRevenueStatus](/API_docs/types/StarsRevenueStatus.html) | Yes|Current balance, current withdrawable balance and overall earned Telegram Stars|
|usd\_rate|[double](/API_docs/types/double.html) | Yes|Current conversion rate of Telegram Stars to USD|



### Type: [payments.StarsRevenueStats](/API_docs/types/payments.StarsRevenueStats.html)


### Example:

```
$payments_starsRevenueStats = ['_' => 'payments.starsRevenueStats', 'top_hours_graph' => StatsGraph, 'revenue_graph' => StatsGraph, 'status' => StarsRevenueStatus, 'usd_rate' => double];
```  
