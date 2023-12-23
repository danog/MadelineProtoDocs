---
title: "messageActionGiftCode"
description: "messageActionGiftCode attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGiftCode  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|via\_giveaway|[Bool](/API_docs/types/Bool.html) | Optional|
|unclaimed|[Bool](/API_docs/types/Bool.html) | Optional|
|boost\_peer|[Peer](/API_docs/types/Peer.html) | Optional|
|months|[int](/API_docs/types/int.html) | Yes|
|slug|[string](/API_docs/types/string.html) | Yes|
|currency|[string](/API_docs/types/string.html) | Optional|
|amount|[long](/API_docs/types/long.html) | Optional|
|crypto\_currency|[string](/API_docs/types/string.html) | Optional|
|crypto\_amount|[long](/API_docs/types/long.html) | Optional|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionGiftCode = ['_' => 'messageActionGiftCode', 'via_giveaway' => Bool, 'unclaimed' => Bool, 'boost_peer' => Peer, 'months' => int, 'slug' => 'string', 'currency' => 'string', 'amount' => long, 'crypto_currency' => 'string', 'crypto_amount' => long];
```  
