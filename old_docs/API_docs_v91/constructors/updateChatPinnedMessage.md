---
title: updateChatPinnedMessage
description: Update chat pinned message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatPinnedMessage  
[Back to constructors index](index.md)



Update chat pinned message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|
|id|[int](../types/int.md) | Yes|ID|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChatPinnedMessage = ['_' => 'updateChatPinnedMessage', 'chat_id' => int, 'id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateChatPinnedMessage", "chat_id": int, "id": int}
```


Or, if you're into Lua:

```lua
updateChatPinnedMessage={_='updateChatPinnedMessage', chat_id=int, id=int}

```


