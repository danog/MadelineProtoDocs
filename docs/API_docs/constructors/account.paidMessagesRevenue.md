---
title: "account.paidMessagesRevenue"
description: "Total number of non-refunded Telegram Stars a user has spent on sending us messages either directly or through a channel, see here » for more info on paid messages."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_paidMessagesRevenue.html
---
# Constructor: account.paidMessagesRevenue  
[Back to constructors index](/API_docs/constructors/index.html)



Total number of non-refunded [Telegram Stars](https://core.telegram.org/api/stars) a user has spent on sending us messages either directly or through a channel, see [here »](https://core.telegram.org/api/paid-messages) for more info on paid messages.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|stars\_amount|[long](/API_docs/types/long.html) | Yes|Amount in [Stars](https://core.telegram.org/api/stars).|



### Type: [account.PaidMessagesRevenue](/API_docs/types/account.PaidMessagesRevenue.html)


### Example:

```
$account_paidMessagesRevenue = ['_' => 'account.paidMessagesRevenue', 'stars_amount' => long];
```  
