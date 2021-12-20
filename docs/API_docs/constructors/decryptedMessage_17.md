---
title: "decryptedMessage"
description: "Contents of an encrypted message."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessage\_17  
[Back to constructors index](index.md)



Contents of an encrypted message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|ttl|[int](../types/int.md) | Yes|Message lifetime. Has higher priority than [decryptedMessageActionSetMessageTTL](../constructors/decryptedMessageActionSetMessageTTL.md).<br>Parameter added in [Layer 17](https://core.telegram.org/api/layers#layer-17).|
|message|[string](../types/string.md) | Yes|Message text|
|media|[DecryptedMessageMedia](../types/DecryptedMessageMedia.md) | Yes|Media content|



### Type: [DecryptedMessage](../types/DecryptedMessage.md)


### Example:

```php
$decryptedMessage_17 = ['_' => 'decryptedMessage', 'ttl' => int, 'message' => 'string', 'media' => DecryptedMessageMedia];
```  


Or, if you're into Lua:

```lua
decryptedMessage_17={_='decryptedMessage', ttl=int, message='string', media=DecryptedMessageMedia}

```


