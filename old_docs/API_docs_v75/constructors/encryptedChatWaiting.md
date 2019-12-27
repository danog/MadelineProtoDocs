---
title: encryptedChatWaiting
description: Chat waiting for approval of second participant.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: encryptedChatWaiting  
[Back to constructors index](index.md)



Chat waiting for approval of second participant.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|Chat ID|
|access\_hash|[long](../types/long.md) | Yes|Checking sum depending on user ID|
|date|[int](../types/int.md) | Yes|Date of chat creation|
|admin\_id|[int](../types/int.md) | Yes|Chat creator ID|
|participant\_id|[int](../types/int.md) | Yes|ID of second chat participant|



### Type: [EncryptedChat](../types/EncryptedChat.md)


### Example:

```php
$encryptedChatWaiting = ['_' => 'encryptedChatWaiting', 'id' => int, 'access_hash' => long, 'date' => int, 'admin_id' => int, 'participant_id' => int];
```  


Or, if you're into Lua:

```lua
encryptedChatWaiting={_='encryptedChatWaiting', id=int, access_hash=long, date=int, admin_id=int, participant_id=int}

```


