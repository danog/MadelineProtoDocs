---
title: updateShortChatMessage
description: Shortened constructor containing info on one new incoming text message from a chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateShortChatMessage  
[Back to constructors index](index.md)



Shortened constructor containing info on one new incoming text message from a chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID of the message|
|from\_id|[int](../types/int.md) | Yes|ID of the sender of the message|
|chat\_id|[int](../types/int.md) | Yes|ID of the chat where the message was sent|
|message|[string](../types/string.md) | Yes|Message|
|pts|[int](../types/int.md) | Yes|[PTS](https://core.telegram.org/api/updates)|
|date|[int](../types/int.md) | Yes|[date](https://core.telegram.org/api/updates)|
|seq|[int](../types/int.md) | Yes|Seq|



### Type: [Updates](../types/Updates.md)


### Example:

```php
$updateShortChatMessage = ['_' => 'updateShortChatMessage', 'id' => int, 'from_id' => int, 'chat_id' => int, 'message' => 'string', 'pts' => int, 'date' => int, 'seq' => int];
```  


Or, if you're into Lua:

```lua
updateShortChatMessage={_='updateShortChatMessage', id=int, from_id=int, chat_id=int, message='string', pts=int, date=int, seq=int}

```


