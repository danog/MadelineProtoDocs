---
title: messageActionChatEditPhoto
description: Group profile changed
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionChatEditPhoto  
[Back to constructors index](index.md)



Group profile changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|photo|[Photo](../types/Photo.md) | Optional|New group pofile photo|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionChatEditPhoto = ['_' => 'messageActionChatEditPhoto', 'photo' => Photo];
```  


Or, if you're into Lua:

```lua
messageActionChatEditPhoto={_='messageActionChatEditPhoto', photo=Photo}

```


