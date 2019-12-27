---
title: messages.sentEncryptedMessage
description: Message without file attachemts sent to an encrypted file.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.sentEncryptedMessage  
[Back to constructors index](index.md)



Message without file attachemts sent to an encrypted file.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|date|[int](../types/int.md) | Yes|Date of sending|



### Type: [messages\_SentEncryptedMessage](../types/messages_SentEncryptedMessage.md)


### Example:

```php
$messages_sentEncryptedMessage = ['_' => 'messages.sentEncryptedMessage', 'date' => int];
```  


Or, if you're into Lua:

```lua
messages_sentEncryptedMessage={_='messages.sentEncryptedMessage', date=int}

```


