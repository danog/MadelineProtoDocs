---
title: messageActionChatEditPhoto
description: Message action chat edit photo
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionChatEditPhoto  
[Back to constructors index](index.md)



Message action chat edit photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|photo|[Photo](../types/Photo.md) | Optional|Photo|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionChatEditPhoto = ['_' => 'messageActionChatEditPhoto', 'photo' => Photo];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageActionChatEditPhoto", "photo": Photo}
```


Or, if you're into Lua:

```lua
messageActionChatEditPhoto={_='messageActionChatEditPhoto', photo=Photo}

```


