---
title: updateEditMessage
description: updateEditMessage attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: updateEditMessage  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|message|[Message](../types/Message.md) | Optional|
|pts|[int](../types/int.md) | Yes|
|pts\_count|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```
$updateEditMessage = ['_' => 'updateEditMessage', 'message' => Message, 'pts' => int, 'pts_count' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateEditMessage", "message": Message, "pts": int, "pts_count": int}
```


Or, if you're into Lua:  


```
updateEditMessage={_='updateEditMessage', message=Message, pts=int, pts_count=int}

```


