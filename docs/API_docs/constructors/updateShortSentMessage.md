---
title: "updateShortSentMessage"
description: "Shortened constructor containing info on one outgoing message to a contact (the destination chat has to be extracted from the method call that returned this object)."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateShortSentMessage  
[Back to constructors index](/API_docs/constructors/index.html)



Shortened constructor containing info on one outgoing message to a contact (the destination chat has to be extracted from the method call that returned this object).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|out|[Bool](/API_docs/types/Bool.html) | Optional|Whether the message is outgoing|
|id|[int](/API_docs/types/int.html) | Yes|ID of the sent message|
|pts|[int](/API_docs/types/int.html) | Yes|[PTS](https://core.telegram.org/api/updates)|
|pts\_count|[int](/API_docs/types/int.html) | Yes|[PTS count](https://core.telegram.org/api/updates)|
|date|[int](/API_docs/types/int.html) | Yes|[date](https://core.telegram.org/api/updates)|
|media|[MessageMedia](/API_docs/types/MessageMedia.html) | Optional|Attached media|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Optional|[Entities](https://core.telegram.org/api/entities) for styled text|
|ttl\_period|[int](/API_docs/types/int.html) | Optional|Time To Live of the message, once message.date+message.ttl\_period === time(), the message will be deleted on the server, and must be deleted locally as well.|



### Type: [Updates](/API_docs/types/Updates.html)


### Example:

```
$updateShortSentMessage = ['_' => 'updateShortSentMessage', 'out' => Bool, 'id' => int, 'pts' => int, 'pts_count' => int, 'date' => int, 'media' => MessageMedia, 'entities' => [MessageEntity, MessageEntity], 'ttl_period' => int];
```  
