---
title: "encryptedMessageService"
description: "Encrypted service message"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: encryptedMessageService  
[Back to constructors index](/API_docs/constructors/index.html)



Encrypted service message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](/API_docs/types/int.html) | Yes|ID of encrypted chat|
|date|[int](/API_docs/types/int.html) | Yes|Date of sending|
|decrypted\_message|[DecryptedMessage](/API_docs/types/DecryptedMessage.html) | Yes|



### Type: [EncryptedMessage](/API_docs/types/EncryptedMessage.html)


### Example:

```
$encryptedMessageService = ['_' => 'encryptedMessageService', 'chat_id' => int, 'date' => int, 'decrypted_message' => DecryptedMessage];
```  
