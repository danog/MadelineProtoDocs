---
title: updateShortSentMessage
description: Update short sent message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateShortSentMessage  
[Back to constructors index](index.md)



Update short sent message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|out|[Bool](../types/Bool.md) | Optional|Out?|
|id|[int](../types/int.md) | Yes|ID|
|pts|[int](../types/int.md) | Yes|Pts|
|pts\_count|[int](../types/int.md) | Yes|Pts count|
|date|[int](../types/int.md) | Yes|Date|
|media|[MessageMedia](../types/MessageMedia.md) | Optional|Media|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|Entities|



### Type: [Updates](../types/Updates.md)


### Example:

```php
$updateShortSentMessage = ['_' => 'updateShortSentMessage', 'out' => Bool, 'id' => int, 'pts' => int, 'pts_count' => int, 'date' => int, 'media' => MessageMedia, 'entities' => [MessageEntity, MessageEntity]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateShortSentMessage", "out": Bool, "id": int, "pts": int, "pts_count": int, "date": int, "media": MessageMedia, "entities": [MessageEntity]}
```


Or, if you're into Lua:

```lua
updateShortSentMessage={_='updateShortSentMessage', out=Bool, id=int, pts=int, pts_count=int, date=int, media=MessageMedia, entities={MessageEntity}}

```


