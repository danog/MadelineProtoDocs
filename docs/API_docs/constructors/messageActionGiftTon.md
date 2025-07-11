---
title: "messageActionGiftTon"
description: "messageActionGiftTon attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGiftTon  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|currency|[string](/API_docs/types/string.html) | Yes|
|amount|[long](/API_docs/types/long.html) | Yes|
|crypto\_currency|[string](/API_docs/types/string.html) | Yes|
|crypto\_amount|[long](/API_docs/types/long.html) | Yes|
|transaction\_id|[string](/API_docs/types/string.html) | Optional|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionGiftTon = ['_' => 'messageActionGiftTon', 'currency' => 'string', 'amount' => long, 'crypto_currency' => 'string', 'crypto_amount' => long, 'transaction_id' => 'string'];
```  
