---
title: "starGiftAttributeOriginalDetails"
description: "starGiftAttributeOriginalDetails attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starGiftAttributeOriginalDetails  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|sender\_id|[Peer](/API_docs/types/Peer.html) | Optional|
|recipient\_id|[Peer](/API_docs/types/Peer.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|
|message|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Optional|



### Type: [StarGiftAttribute](/API_docs/types/StarGiftAttribute.html)


### Example:

```
$starGiftAttributeOriginalDetails = ['_' => 'starGiftAttributeOriginalDetails', 'sender_id' => Peer, 'recipient_id' => Peer, 'date' => int, 'message' => TextWithEntities];
```  
