---
title: "updateNewEncryptedMessage"
description: "New encrypted message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNewEncryptedMessage  
[Back to constructors index](/API_docs/constructors/index.html)



New encrypted message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[EncryptedMessage](/API_docs/types/EncryptedMessage.html) | Yes|Message|
|qts|[int](/API_docs/types/int.html) | Yes|New **qts** value, see [updates »](https://core.telegram.org/api/updates) for more info.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateNewEncryptedMessage = ['_' => 'updateNewEncryptedMessage', 'message' => EncryptedMessage, 'qts' => int];
```  
