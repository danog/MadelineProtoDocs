---
title: "updateEncryptedMessagesRead"
description: "Communication history in an encrypted chat was marked as read."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateEncryptedMessagesRead  
[Back to constructors index](index.md)



Communication history in an encrypted chat was marked as read.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|
|max\_date|[int](../types/int.md) | Yes|Maximum value of data for read messages|
|date|[int](../types/int.md) | Yes|Time when messages were read|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateEncryptedMessagesRead = ['_' => 'updateEncryptedMessagesRead', 'chat_id' => int, 'max_date' => int, 'date' => int];
```  


Or, if you're into Lua:

```lua
updateEncryptedMessagesRead={_='updateEncryptedMessagesRead', chat_id=int, max_date=int, date=int}

```


