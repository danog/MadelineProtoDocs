---
title: inputEncryptedChat
description: Encrypted chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputEncryptedChat  
[Back to constructors index](index.md)



Encrypted chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|



### Type: [InputEncryptedChat](../types/InputEncryptedChat.md)


### Example:

```php
$inputEncryptedChat = ['_' => 'inputEncryptedChat', 'chat_id' => int, 'access_hash' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputEncryptedChat", "chat_id": int, "access_hash": long}
```


Or, if you're into Lua:

```lua
inputEncryptedChat={_='inputEncryptedChat', chat_id=int, access_hash=long}

```


