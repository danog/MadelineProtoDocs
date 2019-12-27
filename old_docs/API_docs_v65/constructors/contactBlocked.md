---
title: contactBlocked
description: A blocked user.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contactBlocked  
[Back to constructors index](index.md)



A blocked user.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User identifier|
|date|[int](../types/int.md) | Yes|Date blacklisted|



### Type: [ContactBlocked](../types/ContactBlocked.md)


### Example:

```php
$contactBlocked = ['_' => 'contactBlocked', 'user_id' => int, 'date' => int];
```  


Or, if you're into Lua:

```lua
contactBlocked={_='contactBlocked', user_id=int, date=int}

```


