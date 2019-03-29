---
title: updates.state
description: State
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updates.state  
[Back to constructors index](index.md)



State

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pts|[int](../types/int.md) | Yes|Pts|
|qts|[int](../types/int.md) | Yes|Qts|
|date|[int](../types/int.md) | Yes|Date|
|seq|[int](../types/int.md) | Yes|Seq|
|unread\_count|[int](../types/int.md) | Yes|Unread count|



### Type: [updates\_State](../types/updates_State.md)


### Example:

```php
$updates_state = ['_' => 'updates.state', 'pts' => int, 'qts' => int, 'date' => int, 'seq' => int, 'unread_count' => int];
```  


Or, if you're into Lua:

```lua
updates_state={_='updates.state', pts=int, qts=int, date=int, seq=int, unread_count=int}

```


