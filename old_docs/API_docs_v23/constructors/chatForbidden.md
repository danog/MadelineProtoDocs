---
title: chatForbidden
description: chatForbidden attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatForbidden  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[int](../types/int.md) | Yes|
|title|[string](../types/string.md) | Yes|
|date|[int](../types/int.md) | Yes|



### Type: [Chat](../types/Chat.md)


### Example:

```
$chatForbidden = ['_' => 'chatForbidden', 'id' => int, 'title' => 'string', 'date' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "chatForbidden", "id": int, "title": "string", "date": int}
```


Or, if you're into Lua:  


```
chatForbidden={_='chatForbidden', id=int, title='string', date=int}

```


