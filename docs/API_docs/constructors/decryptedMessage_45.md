---
title: "decryptedMessage"
description: "Contents of an encrypted message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessage\_45  
[Back to constructors index](/API_docs/constructors/index.html)



Contents of an encrypted message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|ttl|[int](/API_docs/types/int.html) | Yes|Message lifetime. Has higher priority than [decryptedMessageActionSetMessageTTL](../constructors/decryptedMessageActionSetMessageTTL.html).<br>Parameter added in [Layer 17](https://core.telegram.org/api/layers#layer-17).|
|message|[string](/API_docs/types/string.html) | Yes|Message text|
|media|[DecryptedMessageMedia](/API_docs/types/DecryptedMessageMedia.html) | Optional|Media content|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Optional|Message [entities](https://core.telegram.org/api/entities) for styled text (parameter added in layer 45)|
|via\_bot\_name|[string](/API_docs/types/string.html) | Optional|Specifies the ID of the inline bot that generated the message (parameter added in layer 45)|
|reply\_to\_random\_id|[long](/API_docs/types/long.html) | Optional|Random message ID of the message this message replies to (parameter added in layer 45)|



### Type: [DecryptedMessage](/API_docs/types/DecryptedMessage.html)


### Example:

```
$decryptedMessage_45 = ['_' => 'decryptedMessage', 'ttl' => int, 'message' => 'string', 'media' => DecryptedMessageMedia, 'entities' => [MessageEntity, MessageEntity], 'via_bot_name' => 'string', 'reply_to_random_id' => long];
```  
