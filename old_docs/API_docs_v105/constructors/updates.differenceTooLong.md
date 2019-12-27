---
title: updates.differenceTooLong
description: The difference is [too long](https://core.telegram.org/api/updates#recovering-gaps), and the specified state must be used to refetch updates.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updates.differenceTooLong  
[Back to constructors index](index.md)



The difference is [too long](https://core.telegram.org/api/updates#recovering-gaps), and the specified state must be used to refetch updates.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pts|[int](../types/int.md) | Yes|The new state to use.|



### Type: [updates.Difference](../types/updates.Difference.md)


### Example:

```php
$updates.differenceTooLong = ['_' => 'updates.differenceTooLong', 'pts' => int];
```  


Or, if you're into Lua:

```lua
updates.differenceTooLong={_='updates.differenceTooLong', pts=int}

```


