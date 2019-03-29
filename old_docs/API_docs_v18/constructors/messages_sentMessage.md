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
|pts|[int](../types/int.md) | Yes|Pts|
|seq|[int](../types/int.md) | Yes|Seq|



### Type: [messages\_SentMessage](../types/messages_SentMessage.md)


### Example:

```php
$messages_sentMessage = ['_' => 'messages.sentMessage', 'id' => int, 'date' => int, 'pts' => int, 'seq' => int];
```  


Or, if you're into Lua:

```lua
messages_sentMessage={_='messages.sentMessage', id=int, date=int, pts=int, seq=int}

```


