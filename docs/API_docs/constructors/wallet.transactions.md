---
title: "wallet.transactions"
description: "wallet.transactions attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/wallet_transactions.html
---
# Constructor: wallet.transactions  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|balance|[long](/API_docs/types/long.html) | Yes|
|transactions|Array of [WalletTransaction](/API_docs/types/WalletTransaction.html) | Yes|
|next\_offset|[string](/API_docs/types/string.html) | Optional|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [wallet.Transactions](/API_docs/types/wallet.Transactions.html)


### Example:

```
$wallet_transactions = ['_' => 'wallet.transactions', 'balance' => long, 'transactions' => [WalletTransaction, WalletTransaction], 'next_offset' => 'string', 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
