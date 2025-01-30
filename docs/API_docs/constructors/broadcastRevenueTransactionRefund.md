---
title: "broadcastRevenueTransactionRefund"
description: "Describes a refund for failed withdrawal of ad earnings »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: broadcastRevenueTransactionRefund  
[Back to constructors index](/API_docs/constructors/index.html)



Describes a [refund for failed withdrawal of ad earnings »](https://core.telegram.org/api/revenue#withdrawing-revenue)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|amount|[long](/API_docs/types/long.html) | Yes|Amount refunded.|
|date|[int](/API_docs/types/int.html) | Yes|Date of refund.|
|provider|[string](/API_docs/types/string.html) | Yes|Payment provider name.|



### Type: [BroadcastRevenueTransaction](/API_docs/types/BroadcastRevenueTransaction.html)


### Example:

```
$broadcastRevenueTransactionRefund = ['_' => 'broadcastRevenueTransactionRefund', 'amount' => long, 'date' => int, 'provider' => 'string'];
```  
