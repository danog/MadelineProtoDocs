---
title: decryptedMessage
description: decryptedMessage attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessage\_8  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|message|[string](../types/string.md) | Yes|
|media|[DecryptedMessageMedia](../types/DecryptedMessageMedia.md) | Yes|



### Type: [DecryptedMessage](../types/DecryptedMessage.md)


### Example:

```php
$decryptedMessage_8 = ['_' => 'decryptedMessage', 'message' => 'string', 'media' => DecryptedMessageMedia];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "decryptedMessage", "message": "string", "media": DecryptedMessageMedia}
```


Or, if you're into Lua:

```lua
decryptedMessage_8={_='decryptedMessage', message='string', media=DecryptedMessageMedia}

```


