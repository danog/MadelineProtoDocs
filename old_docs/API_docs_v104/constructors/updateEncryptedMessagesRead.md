---
title: updateEncryptedMessagesRead
description: Update encrypted messages read
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateEncryptedMessagesRead  
[Back to constructors index](index.md)



Update encrypted messages read

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|
|max\_date|[int](../types/int.md) | Yes|Max date|
|date|[int](../types/int.md) | Yes|Date|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateEncryptedMessagesRead = ['_' => 'updateEncryptedMessagesRead', 'chat_id' => int, 'max_date' => int, 'date' => int];
```  


Or, if you're into Lua:

```lua
updateEncryptedMessagesRead={_='updateEncryptedMessagesRead', chat_id=int, max_date=int, date=int}

```


