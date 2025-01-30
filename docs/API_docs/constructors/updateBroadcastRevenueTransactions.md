---
title: "updateBroadcastRevenueTransactions"
description: "A new channel ad revenue transaction was made, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBroadcastRevenueTransactions  
[Back to constructors index](/API_docs/constructors/index.html)



A new [channel ad revenue transaction was made, see here »](https://core.telegram.org/api/revenue#revenue-statistics) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|Channel|
|balances|[BroadcastRevenueBalances](/API_docs/types/BroadcastRevenueBalances.html) | Yes|New ad revenue balance.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBroadcastRevenueTransactions = ['_' => 'updateBroadcastRevenueTransactions', 'peer' => long, 'balances' => BroadcastRevenueBalances];
```  
