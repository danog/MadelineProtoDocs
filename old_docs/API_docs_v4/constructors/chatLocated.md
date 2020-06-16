---
title: chatLocated
description: chatLocated attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatLocated  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chat\_id|[int](../types/int.md) | Yes|
|distance|[int](../types/int.md) | Yes|



### Type: [ChatLocated](../types/ChatLocated.md)


### Example:

```php
$chatLocated = ['_' => 'chatLocated', 'chat_id' => int, 'distance' => int];
```  


Or, if you're into Lua:

```lua
chatLocated={_='chatLocated', chat_id=int, distance=int}

```


