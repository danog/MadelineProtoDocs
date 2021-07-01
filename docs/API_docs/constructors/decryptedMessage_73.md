---
title: decryptedMessage
description: Contents of an encrypted message.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessage\_73  
[Back to constructors index](index.md)



Contents of an encrypted message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|ttl|[int](../types/int.md) | Yes|Message lifetime. Has higher priority than [decryptedMessageActionSetMessageTTL](../constructors/decryptedMessageActionSetMessageTTL.md).<br>Parameter added in [Layer 17](https://core.telegram.org/api/layers#layer-17).|
|message|[string](../types/string.md) | Yes|Message text|
|media|[DecryptedMessageMedia](../types/DecryptedMessageMedia.md) | Optional|Media content|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|Message [entities](https://core.telegram.org/api/entities) for styled text (parameter added in layer 45)|
|via\_bot\_name|[string](../types/string.md) | Optional|Specifies the ID of the inline bot that generated the message (parameter added in layer 45)|
|reply\_to\_random\_id|[long](../types/long.md) | Optional|Random message ID of the message this message replies to (parameter added in layer 45)|
|grouped\_id|[long](../types/long.md) | Optional|Random group ID, assigned by the author of message.<br>Multiple encrypted messages with a photo attached and with the same group ID indicate an [album or grouped media](https://core.telegram.org/api/files#albums-grouped-media) (parameter added in layer 45)|



### Type: [DecryptedMessage](../types/DecryptedMessage.md)


### Example:

```php
$decryptedMessage_73 = ['_' => 'decryptedMessage', 'ttl' => int, 'message' => 'string', 'media' => DecryptedMessageMedia, 'entities' => [MessageEntity, MessageEntity], 'via_bot_name' => 'string', 'reply_to_random_id' => long, 'grouped_id' => long];
```  


Or, if you're into Lua:

```lua
decryptedMessage_73={_='decryptedMessage', ttl=int, message='string', media=DecryptedMessageMedia, entities={MessageEntity}, via_bot_name='string', reply_to_random_id=long, grouped_id=long}

```


