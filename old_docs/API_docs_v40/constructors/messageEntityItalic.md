---
title: messageEntityItalic
description: Message entity italic
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityItalic  
[Back to constructors index](index.md)



Message entity italic

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset|
|length|[int](../types/int.md) | Yes|Length|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityItalic = ['_' => 'messageEntityItalic', 'offset' => int, 'length' => int];
```  


Or, if you're into Lua:

```lua
messageEntityItalic={_='messageEntityItalic', offset=int, length=int}

```


