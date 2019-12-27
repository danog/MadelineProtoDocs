---
title: messages.sentEncryptedMessage
description: Message without file attachemts sent to an encrypted file.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_sentEncryptedMessage.html
---
# Constructor: messages.sentEncryptedMessage  
[Back to constructors index](index.md)



Message without file attachemts sent to an encrypted file.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|date|[int](../types/int.md) | Yes|Date of sending|



### Type: [messages.SentEncryptedMessage](../types/messages.SentEncryptedMessage.md)


### Example:

```php
$messages.sentEncryptedMessage = ['_' => 'messages.sentEncryptedMessage', 'date' => int];
```  


Or, if you're into Lua:

```lua
messages.sentEncryptedMessage={_='messages.sentEncryptedMessage', date=int}

```


