---
title: "inputEncryptedChat"
description: "Creates an encrypted chat."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputEncryptedChat  
[Back to constructors index](/API_docs/constructors/index.html)



Creates an encrypted chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](/API_docs/types/int.html) | Yes|Chat ID|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Checking sum from constructor [encryptedChat](../constructors/encryptedChat.html), [encryptedChatWaiting](../constructors/encryptedChatWaiting.html) or [encryptedChatRequested](../constructors/encryptedChatRequested.html)|



### Type: [InputEncryptedChat](/API_docs/types/InputEncryptedChat.html)


### Example:

```
$inputEncryptedChat = ['_' => 'inputEncryptedChat', 'chat_id' => int, 'access_hash' => long];
```  
