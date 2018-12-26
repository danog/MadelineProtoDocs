---
title: updateEditMessage
description: Update edit message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateEditMessage  
[Back to constructors index](index.md)



Update edit message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](../types/Message.md) | Optional|Message|
|pts|[int](../types/int.md) | Yes|Pts|
|pts\_count|[int](../types/int.md) | Yes|Pts count|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateEditMessage = ['_' => 'updateEditMessage', 'message' => Message, 'pts' => int, 'pts_count' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateEditMessage", "message": Message, "pts": int, "pts_count": int}
```


Or, if you're into Lua:

```lua
updateEditMessage={_='updateEditMessage', message=Message, pts=int, pts_count=int}

```


