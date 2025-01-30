---
title: "payments.starsStatus"
description: "Info about the current Telegram Star subscriptions, balance and transaction history »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_starsStatus.html
---
# Constructor: payments.starsStatus  
[Back to constructors index](/API_docs/constructors/index.html)



Info about the current [Telegram Star subscriptions, balance and transaction history »](https://core.telegram.org/api/stars#balance-and-transaction-history).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|balance|[StarsAmount](/API_docs/types/StarsAmount.html) | Yes|Current Telegram Star balance.|
|subscriptions|Array of [StarsSubscription](/API_docs/types/StarsSubscription.html) | Optional|Info about current Telegram Star subscriptions, only returned when invoking [payments.getStarsTransactions](../methods/payments.getStarsTransactions.html) and [payments.getStarsSubscriptions](../methods/payments.getStarsSubscriptions.html).|
|subscriptions\_next\_offset|[string](/API_docs/types/string.html) | Optional|Offset for pagination of subscriptions: only usable and returned when invoking [payments.getStarsSubscriptions](../methods/payments.getStarsSubscriptions.html).|
|subscriptions\_missing\_balance|[long](/API_docs/types/long.html) | Optional|The number of Telegram Stars the user should buy to be able to extend expired subscriptions soon (i.e. the current balance is not enough to extend all expired subscriptions).|
|history|Array of [StarsTransaction](/API_docs/types/StarsTransaction.html) | Optional|List of Telegram Star transactions (partial if `next_offset` is set).|
|next\_offset|[string](/API_docs/types/string.html) | Optional|Offset to use to fetch more transactions from the transaction history using [payments.getStarsTransactions](../methods/payments.getStarsTransactions.html).|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats mentioned in `history`.|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users mentioned in `history`.|



### Type: [payments.StarsStatus](/API_docs/types/payments.StarsStatus.html)


### Example:

```
$payments_starsStatus = ['_' => 'payments.starsStatus', 'balance' => StarsAmount, 'subscriptions' => [StarsSubscription, StarsSubscription], 'subscriptions_next_offset' => 'string', 'subscriptions_missing_balance' => long, 'history' => [StarsTransaction, StarsTransaction], 'next_offset' => 'string', 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
