---
title: "decryptedMessage"
description: "Contents of an encrypted message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessage\_17  
[Back to constructors index](/API_docs/constructors/index.html)



Contents of an encrypted message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|ttl|[int](/API_docs/types/int.html) | Yes|Message lifetime. Has higher priority than [decryptedMessageActionSetMessageTTL](../constructors/decryptedMessageActionSetMessageTTL.html).<br>Parameter added in [Layer 17](https://core.telegram.org/api/layers#layer-17).|
|message|[string](/API_docs/types/string.html) | Yes|Message text|
|media|[DecryptedMessageMedia](/API_docs/types/DecryptedMessageMedia.html) | Yes|Media content|



### Type: [DecryptedMessage](/API_docs/types/DecryptedMessage.html)


### Example:

```
$decryptedMessage_17 = ['_' => 'decryptedMessage', 'ttl' => int, 'message' => 'string', 'media' => DecryptedMessageMedia];
```  
