---
title: "updateEncryptedChatTyping"
description: "Interlocutor is typing a message in an encrypted chat. Update period is 6 second. If upon this time there is no repeated update, it shall be considered that the interlocutor stopped typing."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateEncryptedChatTyping  
[Back to constructors index](/API_docs/constructors/index.html)



Interlocutor is typing a message in an encrypted chat. Update period is 6 second. If upon this time there is no repeated update, it shall be considered that the interlocutor stopped typing.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](/API_docs/types/int.html) | Yes|Chat ID|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateEncryptedChatTyping = ['_' => 'updateEncryptedChatTyping', 'chat_id' => int];
```  
