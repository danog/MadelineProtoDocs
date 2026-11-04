---
title: "payments.starGiftDepositPayload"
description: "payments.starGiftDepositPayload attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_starGiftDepositPayload.html
---
# Constructor: payments.starGiftDepositPayload  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|nft\_address|[string](/API_docs/types/string.html) | Yes|
|payload|[bytes](/API_docs/types/bytes.html) | Yes|
|amount|[long](/API_docs/types/long.html) | Yes|



### Type: [payments.StarGiftDepositPayload](/API_docs/types/payments.StarGiftDepositPayload.html)


### Example:

```
$payments_starGiftDepositPayload = ['_' => 'payments.starGiftDepositPayload', 'nft_address' => 'string', 'payload' => 'bytes', 'amount' => long];
```  
