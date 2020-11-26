---
title: encryptedChatRequested
description: Request to create an encrypted chat.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: encryptedChatRequested  
[Back to constructors index](index.md)



Request to create an encrypted chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|folder\_id|[int](../types/int.md) | Optional|
|id|[int](../types/int.md) | Yes|Chat ID|
|access\_hash|[long](../types/long.md) | Yes|Check sum depending on user ID|
|date|[int](../types/int.md) | Yes|Chat creation date|
|admin\_id|[int](../types/int.md) | Yes|Chat creator ID|
|participant\_id|[int](../types/int.md) | Yes|ID of second chat participant|
|g\_a|[bytes](../types/bytes.md) | Yes|`A = g ^ a mod p`, see [Wikipedia](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)|



### Type: [EncryptedChat](../types/EncryptedChat.md)


### Example:

```php
$encryptedChatRequested = ['_' => 'encryptedChatRequested', 'folder_id' => int, 'id' => int, 'access_hash' => long, 'date' => int, 'admin_id' => int, 'participant_id' => int, 'g_a' => 'bytes'];
```  


Or, if you're into Lua:

```lua
encryptedChatRequested={_='encryptedChatRequested', folder_id=int, id=int, access_hash=long, date=int, admin_id=int, participant_id=int, g_a='bytes'}

```


