---
title: updateNewMessage
description: Update new message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNewMessage  
[Back to constructors index](index.md)



Update new message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](../types/Message.md) | Optional|Message|
|pts|[int](../types/int.md) | Yes|Pts|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateNewMessage = ['_' => 'updateNewMessage', 'message' => Message, 'pts' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateNewMessage", "message": Message, "pts": int}
```


Or, if you're into Lua:

```lua
updateNewMessage={_='updateNewMessage', message=Message, pts=int}

```


