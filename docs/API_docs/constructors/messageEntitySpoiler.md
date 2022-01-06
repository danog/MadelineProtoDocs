---
title: "messageEntitySpoiler"
description: "messageEntitySpoiler attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntitySpoiler  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|offset|[int](../types/int.md) | Yes|
|length|[int](../types/int.md) | Yes|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntitySpoiler = ['_' => 'messageEntitySpoiler', 'offset' => int, 'length' => int];
```  


Or, if you're into Lua:

```lua
messageEntitySpoiler={_='messageEntitySpoiler', offset=int, length=int}

```


