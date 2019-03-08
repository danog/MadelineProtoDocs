---
title: encryptedChatWaiting
description: Encrypted chat waiting
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: encryptedChatWaiting  
[Back to constructors index](index.md)



Encrypted chat waiting

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|date|[int](../types/int.md) | Yes|Date|
|admin\_id|[int](../types/int.md) | Yes|Admin ID|
|participant\_id|[int](../types/int.md) | Yes|Participant ID|



### Type: [EncryptedChat](../types/EncryptedChat.md)


### Example:

```php
$encryptedChatWaiting = ['_' => 'encryptedChatWaiting', 'id' => int, 'access_hash' => long, 'date' => int, 'admin_id' => int, 'participant_id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "encryptedChatWaiting", "id": int, "access_hash": long, "date": int, "admin_id": int, "participant_id": int}
```


Or, if you're into Lua:

```lua
encryptedChatWaiting={_='encryptedChatWaiting', id=int, access_hash=long, date=int, admin_id=int, participant_id=int}

```


