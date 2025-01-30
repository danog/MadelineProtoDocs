---
title: "prepaidStarsGiveaway"
description: "Contains info about a prepaid Telegram Star giveaway »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: prepaidStarsGiveaway  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about a [prepaid Telegram Star giveaway »](https://core.telegram.org/api/giveaways#star-giveaways).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|Prepaid giveaway ID.|
|stars|[long](/API_docs/types/long.html) | Yes|Number of given away [Telegram Stars »](https://core.telegram.org/api/stars)|
|quantity|[int](/API_docs/types/int.html) | Yes|Number of giveaway winners|
|boosts|[int](/API_docs/types/int.html) | Yes|Number of boosts the channel will gain by launching the giveaway.|
|date|[int](/API_docs/types/int.html) | Yes|When was the giveaway paid for|



### Type: [PrepaidGiveaway](/API_docs/types/PrepaidGiveaway.html)


### Example:

```
$prepaidStarsGiveaway = ['_' => 'prepaidStarsGiveaway', 'id' => long, 'stars' => long, 'quantity' => int, 'boosts' => int, 'date' => int];
```  
