---
title: "starGiftAuctionUserState"
description: "starGiftAuctionUserState attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starGiftAuctionUserState  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|returned|[Bool](/API_docs/types/Bool.html) | Optional|
|bid\_amount|[long](/API_docs/types/long.html) | Optional|
|bid\_date|[int](/API_docs/types/int.html) | Optional|
|min\_bid\_amount|[long](/API_docs/types/long.html) | Optional|
|bid\_peer|[Peer](/API_docs/types/Peer.html) | Optional|
|acquired\_count|[int](/API_docs/types/int.html) | Yes|



### Type: [StarGiftAuctionUserState](/API_docs/types/StarGiftAuctionUserState.html)


### Example:

```
$starGiftAuctionUserState = ['_' => 'starGiftAuctionUserState', 'returned' => Bool, 'bid_amount' => long, 'bid_date' => int, 'min_bid_amount' => long, 'bid_peer' => Peer, 'acquired_count' => int];
```  
