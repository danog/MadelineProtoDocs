---
title: updateNewMessage
description: New message in a private chat or in a [legacy group](https://core.telegram.org/api/channel).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNewMessage  
[Back to constructors index](index.md)



New message in a private chat or in a [legacy group](https://core.telegram.org/api/channel).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](../types/Message.md) | Optional|Message|
|pts|[int](../types/int.md) | Yes|New quantity of actions in a message box|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateNewMessage = ['_' => 'updateNewMessage', 'message' => Message, 'pts' => int];
```  


Or, if you're into Lua:

```lua
updateNewMessage={_='updateNewMessage', message=Message, pts=int}

```


