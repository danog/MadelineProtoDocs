---
title: "payments.starGiftOnchainOfferTx"
description: "payments.starGiftOnchainOfferTx attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_starGiftOnchainOfferTx.html
---
# Constructor: payments.starGiftOnchainOfferTx  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|offer\_id|[long](/API_docs/types/long.html) | Yes|
|offer\_address|[string](/API_docs/types/string.html) | Yes|
|expires\_at|[int](/API_docs/types/int.html) | Yes|
|message|[payments.StarGiftOnchainOfferTxMessage](/API_docs/constructors/payments.StarGiftOnchainOfferTxMessage.html) | Yes|
|gasless\_message|[payments.StarGiftOnchainOfferTxMessage](/API_docs/constructors/payments.StarGiftOnchainOfferTxMessage.html) | Optional|
|rent\_budget|[long](/API_docs/types/long.html) | Optional|
|execution\_allowance|[long](/API_docs/types/long.html) | Optional|
|forward\_amount|[long](/API_docs/types/long.html) | Optional|
|fine|[long](/API_docs/types/long.html) | Optional|



### Type: [payments.StarGiftOnchainOfferTx](/API_docs/types/payments.StarGiftOnchainOfferTx.html)


### Example:

```
$payments_starGiftOnchainOfferTx = ['_' => 'payments.starGiftOnchainOfferTx', 'offer_id' => long, 'offer_address' => 'string', 'expires_at' => int, 'message' => payments.StarGiftOnchainOfferTxMessage, 'gasless_message' => payments.StarGiftOnchainOfferTxMessage, 'rent_budget' => long, 'execution_allowance' => long, 'forward_amount' => long, 'fine' => long];
```  
