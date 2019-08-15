---
title: messageEntityBlockquote
description: Quote
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityBlockquote  
[Back to constructors index](index.md)



Quote

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset|
|length|[int](../types/int.md) | Yes|Length|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityBlockquote = ['_' => 'messageEntityBlockquote', 'offset' => int, 'length' => int];
```  


Or, if you're into Lua:

```lua
messageEntityBlockquote={_='messageEntityBlockquote', offset=int, length=int}

```


