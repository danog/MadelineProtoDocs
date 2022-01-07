---
title: "updateShortSentMessage"
description: "Shortened constructor containing info on one outgoing message to a contact (the destination chat has to be extracted from the method call that returned this object)."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateShortSentMessage  
[Back to constructors index](/API_docs/constructors/index.md)



Shortened constructor containing info on one outgoing message to a contact (the destination chat has to be extracted from the method call that returned this object).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|out|[Bool](/API_docs/types/Bool.md) | Optional|Whether the message is outgoing|
|id|[int](/API_docs/types/int.md) | Yes|ID of the sent message|
|pts|[int](/API_docs/types/int.md) | Yes|[PTS](https://core.telegram.org/api/updates)|
|pts\_count|[int](/API_docs/types/int.md) | Yes|[PTS count](https://core.telegram.org/api/updates)|
|date|[int](/API_docs/types/int.md) | Yes|[date](https://core.telegram.org/api/updates)|
|media|[MessageMedia](/API_docs/types/MessageMedia.md) | Optional|Attached media|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.md) | Optional|[Entities](https://core.telegram.org/api/entities) for styled text|
|ttl\_period|[int](/API_docs/types/int.md) | Optional|



### Type: [Updates](/API_docs/types/Updates.md)


### Example:

```php
$updateShortSentMessage = ['_' => 'updateShortSentMessage', 'out' => Bool, 'id' => int, 'pts' => int, 'pts_count' => int, 'date' => int, 'media' => MessageMedia, 'entities' => [MessageEntity, MessageEntity], 'ttl_period' => int];
```  
