---
title: encryptedChatEmpty
description: Empty encrypted chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: encryptedChatEmpty  
[Back to constructors index](index.md)



Empty encrypted chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID|



### Type: [EncryptedChat](../types/EncryptedChat.md)


### Example:

```php
$encryptedChatEmpty = ['_' => 'encryptedChatEmpty', 'id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "encryptedChatEmpty", "id": int}
```


Or, if you're into Lua:

```lua
encryptedChatEmpty={_='encryptedChatEmpty', id=int}

```


