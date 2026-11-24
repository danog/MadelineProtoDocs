---
title: "payments.starGiftOnchainSalePayload"
description: "payments.starGiftOnchainSalePayload attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_starGiftOnchainSalePayload.html
---
# Constructor: payments.starGiftOnchainSalePayload  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|gasless\_available|[Bool](/API_docs/types/Bool.html) | Optional|
|nft\_address|[string](/API_docs/types/string.html) | Yes|
|amount|[long](/API_docs/types/long.html) | Yes|
|payload|[bytes](/API_docs/types/bytes.html) | Yes|



### Type: [payments.StarGiftOnchainSalePayload](/API_docs/types/payments.StarGiftOnchainSalePayload.html)


### Example:

```
$payments_starGiftOnchainSalePayload = ['_' => 'payments.starGiftOnchainSalePayload', 'gasless_available' => Bool, 'nft_address' => 'string', 'amount' => long, 'payload' => 'bytes'];
```  
