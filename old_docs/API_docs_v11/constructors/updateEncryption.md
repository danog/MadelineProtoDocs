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
|encr\_chat|[EncryptedChat](../types/EncryptedChat.md) | Optional|
|date|[int](../types/int.md) | Yes|Date of change|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateEncryption = ['_' => 'updateEncryption', 'encr_chat' => EncryptedChat, 'date' => int];
```  


Or, if you're into Lua:

```lua
updateEncryption={_='updateEncryption', encr_chat=EncryptedChat, date=int}

```


