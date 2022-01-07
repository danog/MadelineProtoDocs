---
title: "inputEncryptedChat"
description: "Creates an encrypted chat."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputEncryptedChat  
[Back to constructors index](/API_docs/constructors/index.md)



Creates an encrypted chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](/API_docs/types/int.md) | Yes|Chat ID|
|access\_hash|[long](/API_docs/types/long.md) | Yes|Checking sum from constructor [encryptedChat](../constructors/encryptedChat.md), [encryptedChatWaiting](../constructors/encryptedChatWaiting.md) or [encryptedChatRequested](../constructors/encryptedChatRequested.md)|



### Type: [InputEncryptedChat](/API_docs/types/InputEncryptedChat.md)


### Example:

```php
$inputEncryptedChat = ['_' => 'inputEncryptedChat', 'chat_id' => int, 'access_hash' => long];
```  
