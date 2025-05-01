---
title: "starsTransaction"
description: "Represents a Telegram Stars transaction »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starsTransaction  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [Telegram Stars transaction »](https://core.telegram.org/api/stars).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|refund|[Bool](/API_docs/types/Bool.html) | Optional|Whether this transaction is a refund.|
|pending|[Bool](/API_docs/types/Bool.html) | Optional|The transaction is currently pending.|
|failed|[Bool](/API_docs/types/Bool.html) | Optional|This transaction has failed.|
|gift|[Bool](/API_docs/types/Bool.html) | Optional|This transaction was a gift from the user in `peer.peer`.|
|reaction|[Bool](/API_docs/types/Bool.html) | Optional|This transaction is a [paid reaction »](https://core.telegram.org/api/reactions#paid-reactions).|
|stargift\_upgrade|[Bool](/API_docs/types/Bool.html) | Optional|
|business\_transfer|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[string](/API_docs/types/string.html) | Yes|Transaction ID.|
|stars|[StarsAmount](/API_docs/types/StarsAmount.html) | Yes|Amount of Stars (negative for outgoing transactions).|
|date|[int](/API_docs/types/int.html) | Yes|Date of the transaction (unixtime).|
|peer|[StarsTransactionPeer](/API_docs/types/StarsTransactionPeer.html) | Yes|Source of the incoming transaction, or its recipient for outgoing transactions.|
|title|[string](/API_docs/types/string.html) | Optional|For transactions with bots, title of the bought product.|
|description|[string](/API_docs/types/string.html) | Optional|For transactions with bots, description of the bought product.|
|photo|[WebDocument](/API_docs/types/WebDocument.html) | Optional|For transactions with bots, photo of the bought product.|
|transaction\_date|[int](/API_docs/types/int.html) | Optional|If neither `pending` nor `failed` are set, the transaction was completed successfully, and this field will contain the point in time (Unix timestamp) when the withdrawal was completed successfully.|
|transaction\_url|[string](/API_docs/types/string.html) | Optional|If neither `pending` nor `failed` are set, the transaction was completed successfully, and this field will contain a URL where the withdrawal transaction can be viewed.|
|bot\_payload|[bytes](/API_docs/types/bytes.html) | Optional|Bot specified invoice payload (i.e. the `payload` passed to [inputMediaInvoice](../constructors/inputMediaInvoice.html) when [creating the invoice](https://core.telegram.org/api/payments)).|
|msg\_id|[int](/API_docs/types/int.html) | Optional|For [paid media transactions »](https://core.telegram.org/api/paid-media), message ID of the paid media posted to `peer.peer` (can point to a deleted message; either way, `extended_media` will always contain the bought media).|
|extended\_media|Array of [MessageMedia](/API_docs/types/MessageMedia.html) | Optional|The purchased [paid media »](https://core.telegram.org/api/paid-media).|
|subscription\_period|[int](/API_docs/types/int.html) | Optional|The number of seconds between consecutive Telegram Star debiting for [Telegram Star subscriptions »](https://core.telegram.org/api/stars#star-subscriptions).|
|giveaway\_post\_id|[int](/API_docs/types/int.html) | Optional|ID of the message containing the [messageMediaGiveaway](../constructors/messageMediaGiveaway.html), for incoming [star giveaway prizes](https://core.telegram.org/api/giveaways#star-giveaways).|
|stargift|[StarGift](/API_docs/types/StarGift.html) | Optional|This transaction indicates a purchase or a sale (conversion back to Stars) of a [gift »](https://core.telegram.org/api/stars).|
|floodskip\_number|[int](/API_docs/types/int.html) | Optional|This transaction is payment for [paid bot broadcasts](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once).  <br>Paid broadcasts are only allowed if the `allow_paid_floodskip` parameter of [messages.sendMessage](../methods/messages.sendMessage.html) and other message sending methods is set while trying to broadcast more than 30 messages per second to bot users. <br>The integer value returned by this flag indicates the number of billed API calls.|
|starref\_commission\_permille|[int](/API_docs/types/int.html) | Optional|This transaction is the receival (or refund) of an [affiliate commission](https://core.telegram.org/api/bots/referrals) (i.e. this is the transaction received by the peer that created the [referral link](https://core.telegram.org/api/links#referral-links), flag 17 is for transactions made by users that imported the referral link).|
|starref\_peer|[Peer](/API_docs/types/Peer.html) | Optional|For transactions made by [referred users](https://core.telegram.org/api/bots/referrals), the peer that received the affiliate commission.|
|starref\_amount|[StarsAmount](/API_docs/types/StarsAmount.html) | Optional|For transactions made by [referred users](https://core.telegram.org/api/bots/referrals), the amount of Telegram Stars received by the affiliate, can be negative for refunds.|
|paid\_messages|[int](/API_docs/types/int.html) | Optional|
|premium\_gift\_months|[int](/API_docs/types/int.html) | Optional|



### Type: [StarsTransaction](/API_docs/types/StarsTransaction.html)


### Example:

```
$starsTransaction = ['_' => 'starsTransaction', 'refund' => Bool, 'pending' => Bool, 'failed' => Bool, 'gift' => Bool, 'reaction' => Bool, 'stargift_upgrade' => Bool, 'business_transfer' => Bool, 'id' => 'string', 'stars' => StarsAmount, 'date' => int, 'peer' => StarsTransactionPeer, 'title' => 'string', 'description' => 'string', 'photo' => WebDocument, 'transaction_date' => int, 'transaction_url' => 'string', 'bot_payload' => 'bytes', 'msg_id' => int, 'extended_media' => [MessageMedia, MessageMedia], 'subscription_period' => int, 'giveaway_post_id' => int, 'stargift' => StarGift, 'floodskip_number' => int, 'starref_commission_permille' => int, 'starref_peer' => Peer, 'starref_amount' => StarsAmount, 'paid_messages' => int, 'premium_gift_months' => int];
```  
