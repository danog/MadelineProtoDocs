---
title: encryptedChatRequested
description: Encrypted chat requested
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: encryptedChatRequested  
[Back to constructors index](index.md)



Encrypted chat requested

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|date|[int](../types/int.md) | Yes|Date|
|admin\_id|[int](../types/int.md) | Yes|Admin ID|
|participant\_id|[int](../types/int.md) | Yes|Participant ID|
|g\_a|[bytes](../types/bytes.md) | Yes|G a|



### Type: [EncryptedChat](../types/EncryptedChat.md)


### Example:

```php
$encryptedChatRequested = ['_' => 'encryptedChatRequested', 'id' => int, 'access_hash' => long, 'date' => int, 'admin_id' => int, 'participant_id' => int, 'g_a' => 'bytes'];
```  


Or, if you're into Lua:

```lua
encryptedChatRequested={_='encryptedChatRequested', id=int, access_hash=long, date=int, admin_id=int, participant_id=int, g_a='bytes'}

```


