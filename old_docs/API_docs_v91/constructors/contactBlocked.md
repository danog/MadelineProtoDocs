---
title: contactBlocked
description: Contact blocked
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contactBlocked  
[Back to constructors index](index.md)



Contact blocked

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|date|[int](../types/int.md) | Yes|Date|



### Type: [ContactBlocked](../types/ContactBlocked.md)


### Example:

```php
$contactBlocked = ['_' => 'contactBlocked', 'user_id' => int, 'date' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "contactBlocked", "user_id": int, "date": int}
```


Or, if you're into Lua:

```lua
contactBlocked={_='contactBlocked', user_id=int, date=int}

```


