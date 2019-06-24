---
title: messageEntityUnderline
description: Underline
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityUnderline  
[Back to constructors index](index.md)



Underline

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset|
|length|[int](../types/int.md) | Yes|Length|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityUnderline = ['_' => 'messageEntityUnderline', 'offset' => int, 'length' => int];
```  


Or, if you're into Lua:

```lua
messageEntityUnderline={_='messageEntityUnderline', offset=int, length=int}

```


