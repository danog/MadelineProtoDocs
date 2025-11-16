---
title: "inputInvoiceStarGiftAuctionBid"
description: "inputInvoiceStarGiftAuctionBid attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputInvoiceStarGiftAuctionBid  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hide\_name|[Bool](/API_docs/types/Bool.html) | Optional|
|update\_bid|[Bool](/API_docs/types/Bool.html) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|gift\_id|[long](/API_docs/types/long.html) | Yes|
|bid\_amount|[long](/API_docs/types/long.html) | Yes|
|message|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Optional|



### Type: [InputInvoice](/API_docs/types/InputInvoice.html)


### Example:

```
$inputInvoiceStarGiftAuctionBid = ['_' => 'inputInvoiceStarGiftAuctionBid', 'hide_name' => Bool, 'update_bid' => Bool, 'peer' => InputPeer, 'gift_id' => long, 'bid_amount' => long, 'message' => TextWithEntities];
```  
