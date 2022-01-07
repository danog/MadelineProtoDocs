---
title: "updateEncryption"
description: "Change of state in an encrypted chat."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateEncryption  
[Back to constructors index](/API_docs/constructors/index.md)



Change of state in an encrypted chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat|[EncryptedChat](/API_docs/types/EncryptedChat.md) | Optional|Encrypted chat|
|date|[int](/API_docs/types/int.md) | Yes|Date of change|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateEncryption = ['_' => 'updateEncryption', 'chat' => EncryptedChat, 'date' => int];
```  
