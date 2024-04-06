---
title: "broadcastRevenueTransactionWithdrawal"
description: "broadcastRevenueTransactionWithdrawal attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: broadcastRevenueTransactionWithdrawal  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|pending|[Bool](/API_docs/types/Bool.html) | Optional|
|failed|[Bool](/API_docs/types/Bool.html) | Optional|
|amount|[long](/API_docs/types/long.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|
|provider|[string](/API_docs/types/string.html) | Yes|
|transaction\_date|[int](/API_docs/types/int.html) | Optional|
|transaction\_url|[string](/API_docs/types/string.html) | Optional|



### Type: [BroadcastRevenueTransaction](/API_docs/types/BroadcastRevenueTransaction.html)


### Example:

```
$broadcastRevenueTransactionWithdrawal = ['_' => 'broadcastRevenueTransactionWithdrawal', 'pending' => Bool, 'failed' => Bool, 'amount' => long, 'date' => int, 'provider' => 'string', 'transaction_date' => int, 'transaction_url' => 'string'];
```  
