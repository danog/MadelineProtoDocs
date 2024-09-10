---
title: "messageActionPrizeStars"
description: "messageActionPrizeStars attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionPrizeStars  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|unclaimed|[Bool](/API_docs/types/Bool.html) | Optional|
|stars|[long](/API_docs/types/long.html) | Yes|
|transaction\_id|[string](/API_docs/types/string.html) | Yes|
|boost\_peer|[Peer](/API_docs/types/Peer.html) | Yes|
|giveaway\_msg\_id|[int](/API_docs/types/int.html) | Yes|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionPrizeStars = ['_' => 'messageActionPrizeStars', 'unclaimed' => Bool, 'stars' => long, 'transaction_id' => 'string', 'boost_peer' => Peer, 'giveaway_msg_id' => int];
```  
