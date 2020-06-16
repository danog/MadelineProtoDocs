---
title: userEmpty
description: Empty constructor, non-existent user.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: userEmpty  
[Back to constructors index](index.md)



Empty constructor, non-existent user.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|User identifier or `0`|



### Type: [User](../types/User.md)


### Example:

```php
$userEmpty = ['_' => 'userEmpty', 'id' => int];
```  


Or, if you're into Lua:

```lua
userEmpty={_='userEmpty', id=int}

```


