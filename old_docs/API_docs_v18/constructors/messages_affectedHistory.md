---
title: messages.affectedHistory
description: Affected history
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.affectedHistory  
[Back to constructors index](index.md)



Affected history

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pts|[int](../types/int.md) | Yes|Pts|
|seq|[int](../types/int.md) | Yes|Seq|
|offset|[int](../types/int.md) | Yes|Offset|



### Type: [messages\_AffectedHistory](../types/messages_AffectedHistory.md)


### Example:

```php
$messages_affectedHistory = ['_' => 'messages.affectedHistory', 'pts' => int, 'seq' => int, 'offset' => int];
```  


Or, if you're into Lua:

```lua
messages_affectedHistory={_='messages.affectedHistory', pts=int, seq=int, offset=int}

```


