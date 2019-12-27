---
title: updateNewEncryptedMessage
description: New encrypted message.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNewEncryptedMessage  
[Back to constructors index](index.md)



New encrypted message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|encr\_message|[EncryptedMessage](../types/EncryptedMessage.md) | Yes|Encr message|
|qts|[int](../types/int.md) | Yes|New **qts** value|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateNewEncryptedMessage = ['_' => 'updateNewEncryptedMessage', 'encr_message' => EncryptedMessage, 'qts' => int];
```  


Or, if you're into Lua:

```lua
updateNewEncryptedMessage={_='updateNewEncryptedMessage', encr_message=EncryptedMessage, qts=int}

```


