---
title: updateEncryptedChatTyping
description: Update encrypted chat typing
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateEncryptedChatTyping  
[Back to constructors index](index.md)



Update encrypted chat typing

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateEncryptedChatTyping = ['_' => 'updateEncryptedChatTyping', 'chat_id' => int];
```  


Or, if you're into Lua:

```lua
updateEncryptedChatTyping={_='updateEncryptedChatTyping', chat_id=int}

```


