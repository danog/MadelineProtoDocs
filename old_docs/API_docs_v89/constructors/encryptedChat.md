---
title: encryptedChat
description: Encrypted chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: encryptedChat  
[Back to constructors index](index.md)



Encrypted chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|date|[int](../types/int.md) | Yes|Date|
|admin\_id|[int](../types/int.md) | Yes|Admin ID|
|participant\_id|[int](../types/int.md) | Yes|Participant ID|
|g\_a\_or\_b|[bytes](../types/bytes.md) | Yes|G a or b|
|key\_fingerprint|[long](../types/long.md) | Yes|Key fingerprint|



### Type: [EncryptedChat](../types/EncryptedChat.md)


### Example:

```php
$encryptedChat = ['_' => 'encryptedChat', 'id' => int, 'access_hash' => long, 'date' => int, 'admin_id' => int, 'participant_id' => int, 'g_a_or_b' => 'bytes', 'key_fingerprint' => long];
```  


Or, if you're into Lua:

```lua
encryptedChat={_='encryptedChat', id=int, access_hash=long, date=int, admin_id=int, participant_id=int, g_a_or_b='bytes', key_fingerprint=long}

```


