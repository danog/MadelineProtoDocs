---
title: "encryptedChatRequested"
description: "Request to create an encrypted chat."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: encryptedChatRequested  
[Back to constructors index](/API_docs/constructors/index.html)



Request to create an encrypted chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|folder\_id|[int](/API_docs/types/int.html) | Optional|[Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders)|
|id|[int](/API_docs/types/int.html) | Yes|Chat ID|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Check sum depending on user ID|
|date|[int](/API_docs/types/int.html) | Yes|Chat creation date|
|admin\_id|[long](/API_docs/types/long.html) | Yes|Chat creator ID|
|participant\_id|[long](/API_docs/types/long.html) | Yes|ID of second chat participant|
|g\_a|[bytes](/API_docs/types/bytes.html) | Yes|`A = g ^ a mod p`, see [Wikipedia](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)|



### Type: [EncryptedChat](/API_docs/types/EncryptedChat.html)


### Example:

```
$encryptedChatRequested = ['_' => 'encryptedChatRequested', 'folder_id' => int, 'id' => int, 'access_hash' => long, 'date' => int, 'admin_id' => long, 'participant_id' => long, 'g_a' => 'bytes'];
```  
