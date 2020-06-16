---
title: chatForbidden
description: A group to which the user has no access. E.g., because the user was kicked from the group.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatForbidden  
[Back to constructors index](index.md)



A group to which the user has no access. E.g., because the user was kicked from the group.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|User identifier|
|title|[string](../types/string.md) | Yes|Group name|
|date|[int](../types/int.md) | Yes|



### Type: [Chat](../types/Chat.md)


### Example:

```php
$chatForbidden = ['_' => 'chatForbidden', 'id' => int, 'title' => 'string', 'date' => int];
```  


Or, if you're into Lua:

```lua
chatForbidden={_='chatForbidden', id=int, title='string', date=int}

```


