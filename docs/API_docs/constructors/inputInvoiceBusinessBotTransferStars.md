---
title: "inputInvoiceBusinessBotTransferStars"
description: "Transfer stars from the balance of a user account connected to a business bot, to the balance of the business bot, see here » for more info on the full flow."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputInvoiceBusinessBotTransferStars  
[Back to constructors index](/API_docs/constructors/index.html)



Transfer stars from the balance of a user account [connected to a business bot](https://core.telegram.org/api/bots/connected-business-bots), to the balance of the [business bot](https://core.telegram.org/api/bots/connected-business-bots), see [here »](https://core.telegram.org/api/stars#transferring-stars-from-a-business-account-to-the-business-bot) for more info on the full flow.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|Always [inputUserSelf](../constructors/inputUserSelf.html).|
|stars|[long](/API_docs/types/long.html) | Yes|The number of stars to transfer.|



### Type: [InputInvoice](/API_docs/types/InputInvoice.html)


### Example:

```
$inputInvoiceBusinessBotTransferStars = ['_' => 'inputInvoiceBusinessBotTransferStars', 'bot' => InputUser, 'stars' => long];
```  
