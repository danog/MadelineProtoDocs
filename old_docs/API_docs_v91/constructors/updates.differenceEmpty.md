---
title: updates.differenceEmpty
description: No events.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/updates_differenceEmpty.html
---
# Constructor: updates.differenceEmpty  
[Back to constructors index](index.md)



No events.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|date|[int](../types/int.md) | Yes|Current date|
|seq|[int](../types/int.md) | Yes|Number of sent updates|



### Type: [updates.Difference](../types/updates.Difference.md)


### Example:

```php
$updates.differenceEmpty = ['_' => 'updates.differenceEmpty', 'date' => int, 'seq' => int];
```  


Or, if you're into Lua:

```lua
updates.differenceEmpty={_='updates.differenceEmpty', date=int, seq=int}

```


