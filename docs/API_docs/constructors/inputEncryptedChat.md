---
title: "inputEncryptedChat"
description: "Creates an encrypted chat."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputEncryptedChat  
[Back to constructors index](index.md)



Creates an encrypted chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|
|access\_hash|[long](../types/long.md) | Yes|Checking sum from constructor [encryptedChat](../constructors/encryptedChat.md), [encryptedChatWaiting](../constructors/encryptedChatWaiting.md) or [encryptedChatRequested](../constructors/encryptedChatRequested.md)|



### Type: [InputEncryptedChat](../types/InputEncryptedChat.md)


### Example:

```php
$inputEncryptedChat = ['_' => 'inputEncryptedChat', 'chat_id' => int, 'access_hash' => long];
```  
