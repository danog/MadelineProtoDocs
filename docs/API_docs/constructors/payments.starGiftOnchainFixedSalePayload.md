---
title: "payments.starGiftOnchainFixedSalePayload"
description: "payments.starGiftOnchainFixedSalePayload attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_starGiftOnchainFixedSalePayload.html
---
# Constructor: payments.starGiftOnchainFixedSalePayload  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|sale\_address|[string](/API_docs/types/string.html) | Yes|
|messages|Array of [payments.StarGiftOnchainOfferTxMessage](/API_docs/constructors/payments.StarGiftOnchainOfferTxMessage.html) | Yes|
|gasless\_messages|Array of [payments.StarGiftOnchainOfferTxMessage](/API_docs/constructors/payments.StarGiftOnchainOfferTxMessage.html) | Optional|



### Type: [payments.StarGiftOnchainSalePayload](/API_docs/types/payments.StarGiftOnchainSalePayload.html)


### Example:

```
$payments_starGiftOnchainFixedSalePayload = ['_' => 'payments.starGiftOnchainFixedSalePayload', 'sale_address' => 'string', 'messages' => [payments.StarGiftOnchainOfferTxMessage, payments.StarGiftOnchainOfferTxMessage], 'gasless_messages' => [payments.StarGiftOnchainOfferTxMessage, payments.StarGiftOnchainOfferTxMessage]];
```  
