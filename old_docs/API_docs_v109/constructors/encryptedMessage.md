---
title: encryptedMessage
description: Encrypted message.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: encryptedMessage  
[Back to constructors index](index.md)



Encrypted message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|ID of encrypted chat|
|date|[int](../types/int.md) | Yes|Date of sending|
|decrypted\_message|[DecryptedMessage](../types/DecryptedMessage.md) | Yes|Decrypted message|
|file|[EncryptedFile](../types/EncryptedFile.md) | Optional|Attached encrypted file|



### Type: [EncryptedMessage](../types/EncryptedMessage.md)


### Example:

```php
$encryptedMessage = ['_' => 'encryptedMessage', 'chat_id' => int, 'date' => int, 'decrypted_message' => DecryptedMessage, 'file' => EncryptedFile];
```  


Or, if you're into Lua:

```lua
encryptedMessage={_='encryptedMessage', chat_id=int, date=int, decrypted_message=DecryptedMessage, file=EncryptedFile}

```


