---
title: "starsTransaction"
description: "starsTransaction attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starsTransaction  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|refund|[Bool](/API_docs/types/Bool.html) | Optional|
|pending|[Bool](/API_docs/types/Bool.html) | Optional|
|failed|[Bool](/API_docs/types/Bool.html) | Optional|
|gift|[Bool](/API_docs/types/Bool.html) | Optional|
|reaction|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[string](/API_docs/types/string.html) | Yes|
|stars|[long](/API_docs/types/long.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|
|peer|[StarsTransactionPeer](/API_docs/types/StarsTransactionPeer.html) | Yes|
|title|[string](/API_docs/types/string.html) | Optional|
|description|[string](/API_docs/types/string.html) | Optional|
|photo|[WebDocument](/API_docs/types/WebDocument.html) | Optional|
|transaction\_date|[int](/API_docs/types/int.html) | Optional|
|transaction\_url|[string](/API_docs/types/string.html) | Optional|
|bot\_payload|[bytes](/API_docs/types/bytes.html) | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Optional|
|extended\_media|Array of [MessageMedia](/API_docs/types/MessageMedia.html) | Optional|
|subscription\_period|[int](/API_docs/types/int.html) | Optional|
|giveaway\_post\_id|[int](/API_docs/types/int.html) | Optional|
|stargift|[StarGift](/API_docs/types/StarGift.html) | Optional|



### Type: [StarsTransaction](/API_docs/types/StarsTransaction.html)


### Example:

```
$starsTransaction = ['_' => 'starsTransaction', 'refund' => Bool, 'pending' => Bool, 'failed' => Bool, 'gift' => Bool, 'reaction' => Bool, 'id' => 'string', 'stars' => long, 'date' => int, 'peer' => StarsTransactionPeer, 'title' => 'string', 'description' => 'string', 'photo' => WebDocument, 'transaction_date' => int, 'transaction_url' => 'string', 'bot_payload' => 'bytes', 'msg_id' => int, 'extended_media' => [MessageMedia, MessageMedia], 'subscription_period' => int, 'giveaway_post_id' => int, 'stargift' => StarGift];
```  
