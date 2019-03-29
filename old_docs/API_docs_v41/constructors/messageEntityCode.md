---
title: messageEntityCode
description: Message entity code
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityCode  
[Back to constructors index](index.md)



Message entity code

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset|
|length|[int](../types/int.md) | Yes|Length|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityCode = ['_' => 'messageEntityCode', 'offset' => int, 'length' => int];
```  


Or, if you're into Lua:

```lua
messageEntityCode={_='messageEntityCode', offset=int, length=int}

```


