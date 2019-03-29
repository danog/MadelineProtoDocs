---
title: updates.differenceEmpty
description: Empty difference
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updates.differenceEmpty  
[Back to constructors index](index.md)



Empty difference

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|date|[int](../types/int.md) | Yes|Date|
|seq|[int](../types/int.md) | Yes|Seq|



### Type: [updates\_Difference](../types/updates_Difference.md)


### Example:

```php
$updates_differenceEmpty = ['_' => 'updates.differenceEmpty', 'date' => int, 'seq' => int];
```  


Or, if you're into Lua:

```lua
updates_differenceEmpty={_='updates.differenceEmpty', date=int, seq=int}

```


