---
title: "updateShortSentMessage"
description: "Shortened constructor containing info on one outgoing message to a contact (the destination chat has to be extracted from the method call that returned this object)."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateShortSentMessage  
[Back to constructors index](index.md)



Shortened constructor containing info on one outgoing message to a contact (the destination chat has to be extracted from the method call that returned this object).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|out|[Bool](../types/Bool.md) | Optional|Whether the message is outgoing|
|id|[int](../types/int.md) | Yes|ID of the sent message|
|pts|[int](../types/int.md) | Yes|[PTS](https://core.telegram.org/api/updates)|
|pts\_count|[int](../types/int.md) | Yes|[PTS count](https://core.telegram.org/api/updates)|
|date|[int](../types/int.md) | Yes|[date](https://core.telegram.org/api/updates)|
|media|[MessageMedia](../types/MessageMedia.md) | Optional|Attached media|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|[Entities](https://core.telegram.org/api/entities) for styled text|
|ttl\_period|[int](../types/int.md) | Optional|



### Type: [Updates](../types/Updates.md)


### Example:

```php
$updateShortSentMessage = ['_' => 'updateShortSentMessage', 'out' => Bool, 'id' => int, 'pts' => int, 'pts_count' => int, 'date' => int, 'media' => MessageMedia, 'entities' => [MessageEntity, MessageEntity], 'ttl_period' => int];
```  


Or, if you're into Lua:

```lua
updateShortSentMessage={_='updateShortSentMessage', out=Bool, id=int, pts=int, pts_count=int, date=int, media=MessageMedia, entities={MessageEntity}, ttl_period=int}

```


