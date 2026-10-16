---
title: "walletTransaction"
description: "walletTransaction attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: walletTransaction  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|incoming|[Bool](/API_docs/types/Bool.html) | Optional|
|failed|[Bool](/API_docs/types/Bool.html) | Optional|
|key\_change|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[string](/API_docs/types/string.html) | Yes|
|amount|[long](/API_docs/types/long.html) | Yes|
|fee|[long](/API_docs/types/long.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|
|peer|[WalletTransactionPeer](/API_docs/types/WalletTransactionPeer.html) | Yes|
|comment|[string](/API_docs/types/string.html) | Optional|
|tx\_hash|[string](/API_docs/types/string.html) | Optional|



### Type: [WalletTransaction](/API_docs/types/WalletTransaction.html)


### Example:

```
$walletTransaction = ['_' => 'walletTransaction', 'incoming' => Bool, 'failed' => Bool, 'key_change' => Bool, 'id' => 'string', 'amount' => long, 'fee' => long, 'date' => int, 'peer' => WalletTransactionPeer, 'comment' => 'string', 'tx_hash' => 'string'];
```  
