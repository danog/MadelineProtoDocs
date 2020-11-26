---
title: updateEncryption
description: Change of state in an encrypted chat.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateEncryption  
[Back to constructors index](index.md)



Change of state in an encrypted chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat|[EncryptedChat](../types/EncryptedChat.md) | Optional|Encrypted chat|
|date|[int](../types/int.md) | Yes|Date of change|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateEncryption = ['_' => 'updateEncryption', 'chat' => EncryptedChat, 'date' => int];
```  


Or, if you're into Lua:

```lua
updateEncryption={_='updateEncryption', chat=EncryptedChat, date=int}

```


