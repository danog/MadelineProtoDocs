---
title: decryptedMessage
description: Contents of an encrypted message.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessage\_8  
[Back to constructors index](index.md)



Contents of an encrypted message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[string](../types/string.md) | Yes|Message text|
|media|[DecryptedMessageMedia](../types/DecryptedMessageMedia.md) | Yes|Media content|



### Type: [DecryptedMessage](../types/DecryptedMessage.md)


### Example:

```php
$decryptedMessage_8 = ['_' => 'decryptedMessage', 'message' => 'string', 'media' => DecryptedMessageMedia];
```  


Or, if you're into Lua:

```lua
decryptedMessage_8={_='decryptedMessage', message='string', media=DecryptedMessageMedia}

```


