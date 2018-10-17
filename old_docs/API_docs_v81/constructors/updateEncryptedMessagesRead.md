---
title: updateEncryptedMessagesRead
description: updateEncryptedMessagesRead attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateEncryptedMessagesRead  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chat\_id|[int](../types/int.md) | Yes|
|max\_date|[int](../types/int.md) | Yes|
|date|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateEncryptedMessagesRead = ['_' => 'updateEncryptedMessagesRead', 'chat_id' => int, 'max_date' => int, 'date' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateEncryptedMessagesRead", "chat_id": int, "max_date": int, "date": int}
```


Or, if you're into Lua:

```lua
updateEncryptedMessagesRead={_='updateEncryptedMessagesRead', chat_id=int, max_date=int, date=int}

```


