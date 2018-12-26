---
title: chatForbidden
description: Chat forbidden
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatForbidden  
[Back to constructors index](index.md)



Chat forbidden

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID|
|title|[string](../types/string.md) | Yes|Title|



### Type: [Chat](../types/Chat.md)


### Example:

```php
$chatForbidden = ['_' => 'chatForbidden', 'id' => int, 'title' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "chatForbidden", "id": int, "title": "string"}
```


Or, if you're into Lua:

```lua
chatForbidden={_='chatForbidden', id=int, title='string'}

```


