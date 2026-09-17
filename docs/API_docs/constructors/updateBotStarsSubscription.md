---
title: "updateBotStarsSubscription"
description: "updateBotStarsSubscription attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotStarsSubscription  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|canceled|[Bool](/API_docs/types/Bool.html) | Optional|
|payment\_failed|[Bool](/API_docs/types/Bool.html) | Optional|
|restored|[Bool](/API_docs/types/Bool.html) | Optional|
|user\_id|[long](/API_docs/types/long.html) | Yes|
|payload|[bytes](/API_docs/types/bytes.html) | Yes|
|qts|[int](/API_docs/types/int.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotStarsSubscription = ['_' => 'updateBotStarsSubscription', 'canceled' => Bool, 'payment_failed' => Bool, 'restored' => Bool, 'user_id' => long, 'payload' => 'bytes', 'qts' => int];
```  
