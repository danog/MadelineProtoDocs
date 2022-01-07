---
title: "updateEncryptedChatTyping"
description: "Interlocutor is typing a message in an encrypted chat. Update period is 6 second. If upon this time there is no repeated update, it shall be considered that the interlocutor stopped typing."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateEncryptedChatTyping  
[Back to constructors index](index.md)



Interlocutor is typing a message in an encrypted chat. Update period is 6 second. If upon this time there is no repeated update, it shall be considered that the interlocutor stopped typing.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateEncryptedChatTyping = ['_' => 'updateEncryptedChatTyping', 'chat_id' => int];
```  
