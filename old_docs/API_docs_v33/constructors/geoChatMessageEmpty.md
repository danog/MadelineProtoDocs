---
title: geoChatMessageEmpty
description: Empty geo chat message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: geoChatMessageEmpty  
[Back to constructors index](index.md)



Empty geo chat message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|
|id|[int](../types/int.md) | Yes|ID|



### Type: [GeoChatMessage](../types/GeoChatMessage.md)


### Example:

```php
$geoChatMessageEmpty = ['_' => 'geoChatMessageEmpty', 'chat_id' => int, 'id' => int];
```  


Or, if you're into Lua:

```lua
geoChatMessageEmpty={_='geoChatMessageEmpty', chat_id=int, id=int}

```


