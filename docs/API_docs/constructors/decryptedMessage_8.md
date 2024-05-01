---
title: "decryptedMessage"
description: "Contents of an encrypted message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessage\_8  
[Back to constructors index](/API_docs/constructors/index.html)



Contents of an encrypted message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[string](/API_docs/types/string.html) | Yes|Message text|
|media|[DecryptedMessageMedia](/API_docs/types/DecryptedMessageMedia.html) | Yes|Media content|



### Type: [DecryptedMessage](/API_docs/types/DecryptedMessage.html)


### Example:

```
$decryptedMessage_8 = ['_' => 'decryptedMessage', 'message' => 'string', 'media' => DecryptedMessageMedia];
```  
