---
title: messageActionChatEditPhoto
description: messageActionChatEditPhoto attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionChatEditPhoto  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|photo|[Photo](../types/Photo.md) | Optional|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```
$messageActionChatEditPhoto = ['_' => 'messageActionChatEditPhoto', 'photo' => Photo];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageActionChatEditPhoto", "photo": Photo}
```


Or, if you're into Lua:  


```
messageActionChatEditPhoto={_='messageActionChatEditPhoto', photo=Photo}

```


