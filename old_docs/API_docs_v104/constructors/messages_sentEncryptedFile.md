---
title: messages.sentEncryptedFile
description: Sent encrypted file
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.sentEncryptedFile  
[Back to constructors index](index.md)



Sent encrypted file

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|date|[int](../types/int.md) | Yes|Date|
|file|[EncryptedFile](../types/EncryptedFile.md) | Optional|File|



### Type: [messages\_SentEncryptedMessage](../types/messages_SentEncryptedMessage.md)


### Example:

```php
$messages_sentEncryptedFile = ['_' => 'messages.sentEncryptedFile', 'date' => int, 'file' => EncryptedFile];
```  


Or, if you're into Lua:

```lua
messages_sentEncryptedFile={_='messages.sentEncryptedFile', date=int, file=EncryptedFile}

```


