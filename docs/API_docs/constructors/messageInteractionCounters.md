---
title: messageInteractionCounters
description: messageInteractionCounters attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageInteractionCounters  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|msg\_id|[int](../types/int.md) | Yes|
|views|[int](../types/int.md) | Yes|
|forwards|[int](../types/int.md) | Yes|



### Type: [MessageInteractionCounters](../types/MessageInteractionCounters.md)


### Example:

```php
$messageInteractionCounters = ['_' => 'messageInteractionCounters', 'msg_id' => int, 'views' => int, 'forwards' => int];
```  


Or, if you're into Lua:

```lua
messageInteractionCounters={_='messageInteractionCounters', msg_id=int, views=int, forwards=int}

```


