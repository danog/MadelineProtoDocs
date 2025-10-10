---
title: "messageActionPrizeStars"
description: "You won some Telegram Stars in a Telegram Star giveaway »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionPrizeStars  
[Back to constructors index](/API_docs/constructors/index.html)



You won some [Telegram Stars](https://core.telegram.org/api/stars) in a [Telegram Star giveaway »](https://core.telegram.org/api/giveaways#star-giveaways).

This service message should be displayed below the appropriate sticker from the [inputStickerSetPremiumGifts »](../constructors/inputStickerSetPremiumGifts.html) [stickerset »](https://core.telegram.org/api/stickers#stickersets):

- If `stars <= 1000`, choose the sticker with emoji equal to "2️⃣"
- If `stars < 2500`, choose the sticker with emoji equal to "3️⃣"
- Otherwise, choose the sticker with emoji equal to "4️⃣"

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|unclaimed|[Bool](/API_docs/types/Bool.html) | Optional|If set, this indicates the reverse transaction that refunds the remaining stars to the creator of a giveaway if, when the giveaway ends, the number of members in the channel is smaller than the number of winners in the giveaway.|
|stars|[long](/API_docs/types/long.html) | Yes|The number of Telegram Stars you won|
|transaction\_id|[string](/API_docs/types/string.html) | Yes|ID of the telegram star transaction.|
|boost\_peer|[Peer](/API_docs/types/Peer.html) | Yes|Identifier of the peer that was automatically boosted by the winners of the giveaway.|
|giveaway\_msg\_id|[int](/API_docs/types/int.html) | Yes|ID of the message containing the [messageMediaGiveaway](../constructors/messageMediaGiveaway.html)|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionPrizeStars = ['_' => 'messageActionPrizeStars', 'unclaimed' => Bool, 'stars' => long, 'transaction_id' => 'string', 'boost_peer' => Peer, 'giveaway_msg_id' => int];
```  
