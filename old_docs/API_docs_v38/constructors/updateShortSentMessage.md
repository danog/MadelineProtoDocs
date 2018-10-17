---
title: updateShortSentMessage
description: updateShortSentMessage attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateShortSentMessage  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[int](../types/int.md) | Yes|
|pts|[int](../types/int.md) | Yes|
|pts\_count|[int](../types/int.md) | Yes|
|date|[int](../types/int.md) | Yes|
|media|[MessageMedia](../types/MessageMedia.md) | Optional|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|



### Type: [Updates](../types/Updates.md)


### Example:

```php
$updateShortSentMessage = ['_' => 'updateShortSentMessage', 'id' => int, 'pts' => int, 'pts_count' => int, 'date' => int, 'media' => MessageMedia, 'entities' => [MessageEntity, MessageEntity]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateShortSentMessage", "id": int, "pts": int, "pts_count": int, "date": int, "media": MessageMedia, "entities": [MessageEntity]}
```


Or, if you're into Lua:

```lua
updateShortSentMessage={_='updateShortSentMessage', id=int, pts=int, pts_count=int, date=int, media=MessageMedia, entities={MessageEntity}}

```


