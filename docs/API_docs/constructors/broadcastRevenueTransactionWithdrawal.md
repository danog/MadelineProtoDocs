---
title: "broadcastRevenueTransactionWithdrawal"
description: "Describes a withdrawal of ad earnings »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: broadcastRevenueTransactionWithdrawal  
[Back to constructors index](/API_docs/constructors/index.html)



Describes a [withdrawal of ad earnings »](https://core.telegram.org/api/revenue#withdrawing-revenue)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pending|[Bool](/API_docs/types/Bool.html) | Optional|Whether the withdrawal is currently pending|
|failed|[Bool](/API_docs/types/Bool.html) | Optional|Whether the withdrawal has failed|
|amount|[long](/API_docs/types/long.html) | Yes|Amount withdrawn|
|date|[int](/API_docs/types/int.html) | Yes|Withdrawal date|
|provider|[string](/API_docs/types/string.html) | Yes|Payment provider name|
|transaction\_date|[int](/API_docs/types/int.html) | Optional|If neither `pending` nor `failed` are set, the transaction was completed successfully, and this field will contain the point in time (Unix timestamp) when the withdrawal was completed successfully.|
|transaction\_url|[string](/API_docs/types/string.html) | Optional|If neither `pending` nor `failed` are set, the transaction was completed successfully, and this field will contain a URL where the withdrawal transaction can be viewed.|



### Type: [BroadcastRevenueTransaction](/API_docs/types/BroadcastRevenueTransaction.html)


### Example:

```
$broadcastRevenueTransactionWithdrawal = ['_' => 'broadcastRevenueTransactionWithdrawal', 'pending' => Bool, 'failed' => Bool, 'amount' => long, 'date' => int, 'provider' => 'string', 'transaction_date' => int, 'transaction_url' => 'string'];
```  
