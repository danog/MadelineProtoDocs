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
|id|[long](../types/long.md) | Yes|
|title|[string](../types/string.md) | Yes|Group name|



### Type: [Chat](../types/Chat.md)


### Example:

```php
$chatForbidden = ['_' => 'chatForbidden', 'id' => long, 'title' => 'string'];
```  


Or, if you're into Lua:

```lua
chatForbidden={_='chatForbidden', id=long, title='string'}

```


