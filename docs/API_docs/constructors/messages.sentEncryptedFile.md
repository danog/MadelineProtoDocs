---
title: "messages.sentEncryptedFile"
description: "Message with a file enclosure sent to a protected chat"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_sentEncryptedFile.html
---
# Constructor: messages.sentEncryptedFile  
[Back to constructors index](/API_docs/constructors/index.html)



Message with a file enclosure sent to a protected chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|date|[int](/API_docs/types/int.html) | Yes|Sending date|
|file|[EncryptedFile](/API_docs/types/EncryptedFile.html) | Optional|Attached file|



### Type: [messages.SentEncryptedMessage](/API_docs/types/messages.SentEncryptedMessage.html)


### Example:

```
$messages_sentEncryptedFile = ['_' => 'messages.sentEncryptedFile', 'date' => int, 'file' => EncryptedFile];
```  
