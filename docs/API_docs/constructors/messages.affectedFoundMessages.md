---
title: "messages.affectedFoundMessages"
description: "messages.affectedFoundMessages attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_affectedFoundMessages.html
---
# Constructor: messages.affectedFoundMessages  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|pts|[int](../types/int.md) | Yes|
|pts\_count|[int](../types/int.md) | Yes|
|offset|[int](../types/int.md) | Yes|
|messages|Array of [int](../types/int.md) | Yes|



### Type: [messages.AffectedFoundMessages](../types/messages.AffectedFoundMessages.md)


### Example:

```php
$messages_affectedFoundMessages = ['_' => 'messages.affectedFoundMessages', 'pts' => int, 'pts_count' => int, 'offset' => int, 'messages' => [int, int]];
```  


Or, if you're into Lua:

```lua
messages_affectedFoundMessages={_='messages.affectedFoundMessages', pts=int, pts_count=int, offset=int, messages={int}}

```


