---
title: "stats.broadcastRevenueWithdrawalUrl"
description: "Contains the URL to use to withdraw channel ad revenue."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stats_broadcastRevenueWithdrawalUrl.html
---
# Constructor: stats.broadcastRevenueWithdrawalUrl  
[Back to constructors index](/API_docs/constructors/index.html)



Contains the URL to use to [withdraw channel ad revenue](https://core.telegram.org/api/revenue#withdrawing-revenue).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](/API_docs/types/string.html) | Yes|A unique URL to a Fragment page where the user will be able to specify and submit the address of the TON wallet where the funds will be sent.|



### Type: [stats.BroadcastRevenueWithdrawalUrl](/API_docs/types/stats.BroadcastRevenueWithdrawalUrl.html)


### Example:

```
$stats_broadcastRevenueWithdrawalUrl = ['_' => 'stats.broadcastRevenueWithdrawalUrl', 'url' => 'string'];
```  
