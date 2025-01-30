---
title: "broadcastRevenueTransactionProceeds"
description: "Describes earnings from sponsored messages in a channel in some time frame, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: broadcastRevenueTransactionProceeds  
[Back to constructors index](/API_docs/constructors/index.html)



Describes earnings from sponsored messages in a channel in some time frame, see [here »](https://core.telegram.org/api/revenue) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|amount|[long](/API_docs/types/long.html) | Yes|Amount in the smallest unit of the cryptocurrency.|
|from\_date|[int](/API_docs/types/int.html) | Yes|Start unixtime for the timeframe.|
|to\_date|[int](/API_docs/types/int.html) | Yes|End unixtime for the timeframe.|



### Type: [BroadcastRevenueTransaction](/API_docs/types/BroadcastRevenueTransaction.html)


### Example:

```
$broadcastRevenueTransactionProceeds = ['_' => 'broadcastRevenueTransactionProceeds', 'amount' => long, 'from_date' => int, 'to_date' => int];
```  
