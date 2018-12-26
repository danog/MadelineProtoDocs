---
title: decryptedMessage
description: Decrypted message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessage\_45  
[Back to constructors index](index.md)



Decrypted message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|ttl|[int](../types/int.md) | Yes|Ttl|
|message|[string](../types/string.md) | Yes|Message|
|media|[DecryptedMessageMedia](../types/DecryptedMessageMedia.md) | Optional|Media|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|Entities|
|via\_bot\_name|[string](../types/string.md) | Optional|Via bot name|
|reply\_to\_random\_id|[long](../types/long.md) | Optional|Reply to random ID|



### Type: [DecryptedMessage](../types/DecryptedMessage.md)


### Example:

```php
$decryptedMessage_45 = ['_' => 'decryptedMessage', 'ttl' => int, 'message' => 'string', 'media' => DecryptedMessageMedia, 'entities' => [MessageEntity, MessageEntity], 'via_bot_name' => 'string', 'reply_to_random_id' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "decryptedMessage", "ttl": int, "message": "string", "media": DecryptedMessageMedia, "entities": [MessageEntity], "via_bot_name": "string", "reply_to_random_id": long}
```


Or, if you're into Lua:

```lua
decryptedMessage_45={_='decryptedMessage', ttl=int, message='string', media=DecryptedMessageMedia, entities={MessageEntity}, via_bot_name='string', reply_to_random_id=long}

```


