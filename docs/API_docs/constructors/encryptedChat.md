---
title: "encryptedChat"
description: "Encrypted chat"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: encryptedChat  
[Back to constructors index](/API_docs/constructors/index.html)



Encrypted chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](/API_docs/types/int.html) | Yes|Chat ID|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Check sum dependent on the user ID|
|date|[int](/API_docs/types/int.html) | Yes|Date chat was created|
|admin\_id|[long](/API_docs/types/long.html) | Yes|Chat creator ID|
|participant\_id|[long](/API_docs/types/long.html) | Yes|ID of the second chat participant|
|g\_a\_or\_b|[bytes](/API_docs/types/bytes.html) | Yes|`B = g ^ b mod p`, if the currently authorized user is the chat's creator,<br>or `A = g ^ a mod p` otherwise<br>See [Wikipedia](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange) for more info|
|key\_fingerprint|[long](/API_docs/types/long.html) | Yes|64-bit fingerprint of received key|



### Type: [EncryptedChat](/API_docs/types/EncryptedChat.html)


### Example:

```
$encryptedChat = ['_' => 'encryptedChat', 'id' => int, 'access_hash' => long, 'date' => int, 'admin_id' => long, 'participant_id' => long, 'g_a_or_b' => 'bytes', 'key_fingerprint' => long];
```  
