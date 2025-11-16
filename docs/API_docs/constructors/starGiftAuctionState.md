---
title: "starGiftAuctionState"
description: "starGiftAuctionState attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starGiftAuctionState  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|version|[int](/API_docs/types/int.html) | Yes|
|start\_date|[int](/API_docs/types/int.html) | Yes|
|end\_date|[int](/API_docs/types/int.html) | Yes|
|min\_bid\_amount|[long](/API_docs/types/long.html) | Yes|
|bid\_levels|Array of [AuctionBidLevel](/API_docs/types/AuctionBidLevel.html) | Yes|
|top\_bidders|Array of [long](/API_docs/types/long.html) | Yes|
|next\_round\_at|[int](/API_docs/types/int.html) | Yes|
|gifts\_left|[int](/API_docs/types/int.html) | Yes|
|current\_round|[int](/API_docs/types/int.html) | Yes|
|total\_rounds|[int](/API_docs/types/int.html) | Yes|



### Type: [StarGiftAuctionState](/API_docs/types/StarGiftAuctionState.html)


### Example:

```
$starGiftAuctionState = ['_' => 'starGiftAuctionState', 'version' => int, 'start_date' => int, 'end_date' => int, 'min_bid_amount' => long, 'bid_levels' => [AuctionBidLevel, AuctionBidLevel], 'top_bidders' => [long, long], 'next_round_at' => int, 'gifts_left' => int, 'current_round' => int, 'total_rounds' => int];
```  
