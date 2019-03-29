---
title: messages.sentMessage
description: Sent message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.sentMessage  
[Back to constructors index](index.md)



Sent message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID|
|date|[int](../types/int.md) | Yes|Date|
|media|[MessageMedia](../types/MessageMedia.md) | Optional|Media|
|pts|[int](../types/int.md) | Yes|Pts|
|pts\_count|[int](../types/int.md) | Yes|Pts count|



### Type: [messages\_SentMessage](../types/messages_SentMessage.md)


### Example:

```php
$messages_sentMessage = ['_' => 'messages.sentMessage', 'id' => int, 'date' => int, 'media' => MessageMedia, 'pts' => int, 'pts_count' => int];
```  


Or, if you're into Lua:

```lua
messages_sentMessage={_='messages.sentMessage', id=int, date=int, media=MessageMedia, pts=int, pts_count=int}

```


