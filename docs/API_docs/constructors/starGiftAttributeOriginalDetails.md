---
title: "starGiftAttributeOriginalDetails"
description: "Info about the sender, receiver and message attached to the original gift », before it was upgraded to a collectible gift »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starGiftAttributeOriginalDetails  
[Back to constructors index](/API_docs/constructors/index.html)



Info about the sender, receiver and message attached to the original [gift »](https://core.telegram.org/api/gifts), before it was upgraded to a [collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|sender\_id|[Peer](/API_docs/types/Peer.html) | Optional|Original sender of the gift, absent if the gift was private.|
|recipient\_id|[Peer](/API_docs/types/Peer.html) | Yes|Original receiver of the gift.|
|date|[int](/API_docs/types/int.html) | Yes|When was the gift sent.|
|message|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Optional|Original message attached to the gift, if present.|



### Type: [StarGiftAttribute](/API_docs/types/StarGiftAttribute.html)


### Example:

```
$starGiftAttributeOriginalDetails = ['_' => 'starGiftAttributeOriginalDetails', 'sender_id' => Peer, 'recipient_id' => Peer, 'date' => int, 'message' => TextWithEntities];
```  
