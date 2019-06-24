---
title: messageRange
description: Message range
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageRange  
[Back to constructors index](index.md)



Message range

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|min\_id|[int](../types/int.md) | Yes|Min ID|
|max\_id|[int](../types/int.md) | Yes|Max ID|



### Type: [MessageRange](../types/MessageRange.md)


### Example:

```php
$messageRange = ['_' => 'messageRange', 'min_id' => int, 'max_id' => int];
```  


Or, if you're into Lua:

```lua
messageRange={_='messageRange', min_id=int, max_id=int}

```


