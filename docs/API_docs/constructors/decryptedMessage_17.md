---
title: decryptedMessage
description: Decrypted message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessage\_17  
[Back to constructors index](index.md)



Decrypted message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|ttl|[int](../types/int.md) | Yes|Ttl|
|message|[string](../types/string.md) | Yes|Message|
|media|[DecryptedMessageMedia](../types/DecryptedMessageMedia.md) | Yes|Media|



### Type: [DecryptedMessage](../types/DecryptedMessage.md)


### Example:

```php
$decryptedMessage_17 = ['_' => 'decryptedMessage', 'ttl' => int, 'message' => 'string', 'media' => DecryptedMessageMedia];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "decryptedMessage", "ttl": int, "message": "string", "media": DecryptedMessageMedia}
```


Or, if you're into Lua:

```lua
decryptedMessage_17={_='decryptedMessage', ttl=int, message='string', media=DecryptedMessageMedia}

```


