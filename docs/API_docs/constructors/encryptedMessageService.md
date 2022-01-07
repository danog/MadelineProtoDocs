---
title: "encryptedMessageService"
description: "Encrypted service message"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: encryptedMessageService  
[Back to constructors index](/API_docs/constructors/index.md)



Encrypted service message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](/API_docs/types/int.md) | Yes|ID of encrypted chat|
|date|[int](/API_docs/types/int.md) | Yes|Date of sending|
|decrypted\_message|[DecryptedMessage](/API_docs/types/DecryptedMessage.md) | Yes|



### Type: [EncryptedMessage](/API_docs/types/EncryptedMessage.md)


### Example:

```php
$encryptedMessageService = ['_' => 'encryptedMessageService', 'chat_id' => int, 'date' => int, 'decrypted_message' => DecryptedMessage];
```  
