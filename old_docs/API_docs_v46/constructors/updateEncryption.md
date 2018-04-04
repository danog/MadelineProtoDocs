---
title: updateEncryption
description: updateEncryption attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: updateEncryption  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|encr\_chat|[EncryptedChat](../types/EncryptedChat.md) | Optional|
|date|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```
$updateEncryption = ['_' => 'updateEncryption', 'encr_chat' => EncryptedChat, 'date' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateEncryption", "encr_chat": EncryptedChat, "date": int}
```


Or, if you're into Lua:  


```
updateEncryption={_='updateEncryption', encr_chat=EncryptedChat, date=int}

```


