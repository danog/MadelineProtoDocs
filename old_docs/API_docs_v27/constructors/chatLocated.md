---
title: chatLocated
description: Chat located
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatLocated  
[Back to constructors index](index.md)



Chat located

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|
|distance|[int](../types/int.md) | Yes|Distance|



### Type: [ChatLocated](../types/ChatLocated.md)


### Example:

```php
$chatLocated = ['_' => 'chatLocated', 'chat_id' => int, 'distance' => int];
```  


Or, if you're into Lua:

```lua
chatLocated={_='chatLocated', chat_id=int, distance=int}

```


