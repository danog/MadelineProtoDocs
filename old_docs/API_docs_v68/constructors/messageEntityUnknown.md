---
title: messageEntityUnknown
description: Message entity unknown
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityUnknown  
[Back to constructors index](index.md)



Message entity unknown

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset|
|length|[int](../types/int.md) | Yes|Length|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityUnknown = ['_' => 'messageEntityUnknown', 'offset' => int, 'length' => int];
```  


Or, if you're into Lua:

```lua
messageEntityUnknown={_='messageEntityUnknown', offset=int, length=int}

```


