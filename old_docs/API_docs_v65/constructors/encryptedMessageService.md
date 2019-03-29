---
title: encryptedMessageService
description: Encrypted message service
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: encryptedMessageService  
[Back to constructors index](index.md)



Encrypted message service

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|
|date|[int](../types/int.md) | Yes|Date|
|decrypted\_message|[DecryptedMessage](../types/DecryptedMessage.md) | Yes|Decrypted message|



### Type: [EncryptedMessage](../types/EncryptedMessage.md)


### Example:

```php
$encryptedMessageService = ['_' => 'encryptedMessageService', 'chat_id' => int, 'date' => int, 'decrypted_message' => DecryptedMessage];
```  


Or, if you're into Lua:

```lua
encryptedMessageService={_='encryptedMessageService', chat_id=int, date=int, decrypted_message=DecryptedMessage}

```


