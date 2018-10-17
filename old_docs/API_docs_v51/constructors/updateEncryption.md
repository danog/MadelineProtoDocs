---
title: updateEncryption
description: updateEncryption attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateEncryption  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chat|[EncryptedChat](../types/EncryptedChat.md) | Optional|
|date|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateEncryption = ['_' => 'updateEncryption', 'chat' => EncryptedChat, 'date' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateEncryption", "chat": EncryptedChat, "date": int}
```


Or, if you're into Lua:

```lua
updateEncryption={_='updateEncryption', chat=EncryptedChat, date=int}

```


